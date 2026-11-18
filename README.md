# my-docker-app (Python / Flask)

## Run locally
    pip install -r requirements-dev.txt
    pytest
    docker build -t my-docker-app .
    docker run -p 5000:5000 my-docker-app     # open http://localhost:5000

## CI/CD
Push to `main` -> tests run -> image is built -> pushed to
`ghcr.io/<your-github-username>/my-docker-app:latest`
