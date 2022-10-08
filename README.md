# Baiter Basic Honeypot

#### Flask app for collecting information about malicious HTTP requests.

Baiter honeypot is project created to understand most basic vulnerabilities that web apps are facing today. Internet
bots are continuously crawling the web and sending malicious requests to random web apps. Most of these attacks are
easily preventable by correct application configuration, and keeping libraries up to date.

Project is created based on logs from 15 days of POC web app, that was collecting logs about the attacks.
The most common malicious requests will be counted and mocked.

#### Project will contain:

- Web vulnerabilities on port `80`:
    - Wordpress 
    - PHP
    - Path traversal
    - Cross Site Scripting
- mock SQL db on port `8123`
- mock SSH client on port `22`

## Getting Started

Application uses docker-compose, to build and run all the dependencies.
To run application run `docker compose up`

## Contributing

If you want to contribute to Baiter go ahead and create pull request.

## License

This project is licensed under the MIT - see the [LICENSE](LICENSE) file for details

