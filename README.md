# autoNote
<!-- TO RUN: -->

ADD: .env file to the root of the project
Sample:
  DATABASE_URI=your-db-url
  FLASK_DEBUG=True
  SECRET_KEY=can-be-any-secret

  OPENAI_API_KEY=your-open-ai-key
  STABILITY_API_KEY=your-stability-ai-key

  SPACE_REGION=your-digital-ocean-space-regoin
  SPACE_NAME=your-digital-ocean-space-name
  SPACE_KEY=your-digital-ocean-space-key
  SPACE_SECRET=your-digital-ocean-space-secret
  SPACE_ENDPOINT=your-digital-ocean-space-endpoint
  SPACE_EDGE_ENDPOINT=your-digital-ocean-space-edge-endpoint-or-just-the-end-point-again

Install Python on your computer
RUN: pip install -r requirements.txt
RUN: export FLASK_APP=main.py
RUN: flask run
