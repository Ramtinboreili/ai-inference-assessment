
###################################################################################################
# AIAhura Tech — DevOps Technical Assessment
# Project: AI Inference Service
# This repository is part of AIAhura Tech's DevOps engineer interview process.
# All work submitted will be evaluated for technical quality, security practices, and documentation.
###################################################################################################
import os
import time
import redis
from functools import wraps
from fastapi import HTTPException
import logging

# TODO: Implement a Redis-backed rate limiter decorator
# Suggested signature: rate_limiter(max_per_min: int = 60) -> Callable
# Use REDIS_URL env var; fail open if Redis is unavailable.
# raise NotImplementedError("Implement Redis-based rate limiter")

logger = logging.getLogger("app.rate_limit")
logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

def rate_limit(max_per_min: int = 60):
    """
    Redis-based rate limiter decorator.
    Limits requests to max_per_min per minute per client IP.
    Fails open if Redis is unavailable.
    """
    redis_client = None
    try:
        redis_client = redis.Redis.from_url(
            os.getenv("REDIS_URL", "redis://redis:6379/0"),
            decode_responses=True
        )
        # Test Redis connection
        redis_client.ping()
    except redis.ConnectionError as e:
        logger.warning(f"Redis connection failed: {e}. Rate limiting will fail open.")
        redis_client = None

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, request: "fastapi.Request", **kwargs):
            if redis_client is None:
                logger.info("Rate limiting disabled due to Redis unavailability")
                return await func(*args, request=request, **kwargs)

            # Use client IP as the key for rate limiting
            client_ip = request.client.host
            key = f"rate_limit:{client_ip}:{int(time.time() // 60)}"
            
            try:
                # Increment request count and set expiry for 60 seconds
                count = redis_client.incr(key)
                if count == 1:
                    redis_client.expire(key, 60)
                
                if count > max_per_min:
                    logger.warning(f"Rate limit exceeded for IP {client_ip}: {count} requests")
                    raise HTTPException(status_code=429, detail="Rate limit exceeded")
                
                logger.debug(f"Request allowed for IP {client_ip}: {count}/{max_per_min}")
                return await func(*args, request=request, **kwargs)
            
            except redis.RedisError as e:
                logger.error(f"Redis error during rate limiting: {e}. Failing open.")
                return await func(*args, request=request, **kwargs)
        
        return wrapper
    return decorator