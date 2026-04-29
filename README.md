# Address Coordinates Decoder

This project is a small Python command-line application that converts an address
or place name into geographic coordinates. It uses the `geopy` library and the
OpenStreetMap Nominatim geocoding service.

The project was created as a Docker containerization exercise. It includes the
Python application code, dependency list, Dockerfile, build and run commands, and
the final Docker Hub image tag.

## Project Files

- `app.py` - Python source code for the address-to-coordinates application.
- `requirements.txt` - Python dependency list.
- `Dockerfile` - Docker image build instructions.
- `.dockerignore` - Files excluded from the Docker build context.

## Run Locally

Install the required Python dependency:

```bash
pip install -r requirements.txt
```

Run the app with an address:

```bash
python app.py "Gedimino pr. 1, Vilnius, Lithuania"
```

Example output:

```text
Search: Gedimino pr. 1, Vilnius, Lithuania
Matched address: 1, Gedimino pr., Senamiestis, Senamiesčio seniūnija, Vilnius, Vilniaus miesto savivaldybė, Vilniaus apskritis, 01103, Lietuva
Latitude: 54.686236
Longitude: 25.285994
```

## Build the Docker Image

```bash
docker build -t address-coordinates-decoder:1.0 .
```

## Run the Docker Container

```bash
docker run --rm address-coordinates-decoder:1.0 "Gedimino pr. 1, Vilnius, Lithuania"
```

The same image can also be run from Docker Hub:

```bash
docker run --rm ausrbu/address-coordinates-decoder:1.0 "Gedimino pr. 1, Vilnius, Lithuania"
```

## Push the Docker Image to Docker Hub

Log in to Docker Hub:

```bash
docker login
```

Tag the image:

```bash
docker tag address-coordinates-decoder:1.0 ausrbu/address-coordinates-decoder:1.0
```

Push the image:

```bash
docker push ausrbu/address-coordinates-decoder:1.0
```

Final Docker Hub image tag:

```text
ausrbu/address-coordinates-decoder:1.0
```

Image digest from the successful push:


## Notes

The application requires internet access because it sends the address query to
the Nominatim geocoding service. If the address cannot be found, the app exits
with a clear error message.
