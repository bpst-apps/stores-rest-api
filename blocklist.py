"""
blocklist.py

This file just contains the blocklist of the JWT tokens.It will be imported by app and the logout resource so that tokens can be added to blocklist when the user logs out.

"""

# Save blocklist in database: use redis
BLOCKLIST = set()