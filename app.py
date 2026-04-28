import argparse
import sys
from typing import Optional

from geopy.exc import GeocoderServiceError, GeocoderTimedOut
from geopy.geocoders import Nominatim


def geocode_address(address: str) -> Optional[tuple[float, float, str]]:
    """Convert an address into latitude, longitude, and a formatted address."""
    geolocator = Nominatim(user_agent="address-coordinates-decoder")
    location = geolocator.geocode(address, timeout=10)

    if location is None:
        return None

    return location.latitude, location.longitude, location.address


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert an address or place name into geographic coordinates."
    )
    parser.add_argument(
        "address",
        help='Address to search, for example: "Gedimino pr. 1, Vilnius, Lithuania"',
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    address = args.address.strip()

    if not address:
        print("Error: address cannot be empty.", file=sys.stderr)
        return 1

    try:
        result = geocode_address(address)
    except GeocoderTimedOut:
        print("Error: geocoding service timed out. Please try again.", file=sys.stderr)
        return 1
    except GeocoderServiceError as error:
        print(f"Error: geocoding service failed: {error}", file=sys.stderr)
        return 1

    if result is None:
        print(f'No coordinates found for: "{address}"', file=sys.stderr)
        return 1

    latitude, longitude, matched_address = result

    print(f"Search: {address}")
    print(f"Matched address: {matched_address}")
    print(f"Latitude: {latitude:.6f}")
    print(f"Longitude: {longitude:.6f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
