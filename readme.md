<!-- PROJECT LOGO -->
<h3 align="center">MT5 API by Sunwaee</h3>
<p align="center">
This project aims to deploy APIs using sunwaee-mt5-template models.
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#aknowledgments">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This project aims to deploy transformers APIs.

### Built With

* [Python 3.8](https://www.python.org/)



<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

There are no prerequisites other than those of requirements.txt.

### Installation

1. Clone the repo
    ```sh
    path/to/folder$ git clone https://github.com/Sunwaee/sunwaee-mt5-api.git
    ```
2. Install necessary packages
    ```sh
    path/to/folder/sunwaee-mt5-template$ pip install -r requirements.txt
    ```



<!-- USAGE EXAMPLES -->

## Usage

1. Add a route and customize your requests processing
    ```python
    @app.get(path="/classic", tags=['inference'])
    async def classic(text: str = ""):
        """
        Infers using classic pipeline.
    
            :param text: text on which apply classic task
            :return: dictionary which contains classic output
        """

        start = time.time()
        language = language_detector.predict(text=[text])
        output = classic_pipeline(inputs=text)
        reponse_time = time.time() - start
    
        return {
            "input": text,
            "language": language[0][0][0].replace("__label__", ""),
            "output": output,
            "response time": reponse_time
        }
    ```

2. Run the api in a first terminal
    ```shell
    path/to/sunwaee-mt5-api$ uvicorn api:app --reload
    ```
   
3. Run ngrok for public hosting
    ```shell
    path/to/sunwaee-mt5-api$ ngrok http 8000
    ```
    > Note that you must copy the link you'll get in ngrok terminal and add **/docs/** at the end to access the public API.

<!-- LICENSE -->

## License

Distributed under the MIT License. See `License` for more information.

```quote
@misc{sunwaee-mt5-api,
    author = {David NAISSE - @Sunwaee},
    title = {MT5 API},
    publisher = {GitHub},
    journal = {GitHub repository},
    year = {2021},
    howpublished={\url{https://github.com/Sunwaee/sunwaee-mt5-api}}
}
```

<!-- CONTACT -->

## Contact

@Sunwaee - sunwaee.contact@gmail.com - [LinkedIn](https://www.linkedin.com/in/dvdnss/)

Project Link: [https://github.com/Sunwaee/sunwaee-mt5-api](https://github.com/Sunwaee/sunwaee-mt5-api)



<!-- AKNOWLEDGEMENTS -->

## Acknowledgements

* [HuggingFace](https://huggingface.co/) (no need to talk about it)
* [GitHub](https://github.com/) (sometimes we forget to mention it)
* [othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) (should be set by default in
  any git)
* [FastAPI](https://fastapi.tiangolo.com/) (easy Python APIs)
* [Ngrok](https://ngrok.com/) (easy & free tunneling)