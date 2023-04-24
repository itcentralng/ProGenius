# ProposalAI Flask Server

The Proposal Flask server is a backend service for the [ProGenius ReactJs app](https://github.com/itcentralng/ProGeniusApp). The server uses AI21 to generate contents of a proposal for business persons. The server can handle simple prompts such as name of company, name of client company and short description about the proposal.

## TO RUN:

To run the ProposalAI Flask server, follow the steps below:

1. Add a `.env` file to the root of the project with the following details:
    ```
    DATABASE_URI=your-db-url
    FLASK_DEBUG=True
    SECRET_KEY=can-be-any-secret
    
    SPACE_REGION=your-do-space-region
    SPACE_NAME=your-do-space-name
    SPACE_KEY=your-do-space-key
    SPACE_SECRET=your-do-space-secret
    SPACE_ENDPOINT=your-do-space-endpoint
    SPACE_EDGE_ENDPOINT=your-do-space-endpoint

    CELERY_BROKER_URL=your-redis-string
    result_backend=your-redis-string

    AI21_API_KEY=your-open-ai-key
    ```
   Note that you'll need to obtain the necessary API keys to fill out the values.

2. Install Python on your computer.

3. Install dependencies by running `pip install -r requirements.txt`.

4. Set the `FLASK_APP` environment variable to `main.py` by running `export FLASK_APP=main.py`.

5. Run migration by running `flask db upgrade`.

6. Start the Flask server by running `flask run`.

## Endpoints

The following endpoints are available:

- `/company` - (GET, POST, PATCH, DELETE)
- `/client` - (GET, POST, PATCH, DELETE)
- `/proposal` - (GET, POST, PATCH, DELETE)
- `/components` - (GET: get a list of available components to add to your proposal)

### Request Parameters

The `/company` endpoint accepts the following parameters in a JSON payload:

- `name`
- `address`
- `description`
- `rep`
- `role`
- `phone`
- `email`

The `/client` endpoint accepts the following parameters in a JSON payload:

- `name`
- `address`
- `description`
- `rep`
- `role`
- `phone`
- `email`

The `/proposal` endpoint accepts the following parameters in a JSON payload:

- `company_id`
- `client_id`
- `offering`
- `description`

The `/proposal/<id>` endpoint accepts the following parameters in a JSON payload:

- `component`
- `index`

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome any contributions or suggestions that can improve the application's functionality.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

This project makes use of the following libraries and APIs:

- Flask
- AI21 API
