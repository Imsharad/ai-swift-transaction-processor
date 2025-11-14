To make sure you can get started on the project right away without any setup, we've provided a **VS Code workspace** on the following pages.

The project's starter files are already loaded, and all the necessary Python libraries are installed.

## Local Machine Instructions

While this project is ready to go in the online VS Code workspace on the following page, you can also set it up on your local machine. Following these steps will help you create a consistent environment for development.

#### **Step 1: Prerequisites**

Before you begin, make sure you have the following installed on your system:

* **Python 3.10 or newer** : This project relies on features available in modern versions of Python. You can check your Python version by opening a terminal or command prompt and running:

<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f"><div class="css-1wj0762"></div><div><code class="language-bash"><span>python --version</span></code></div></div></pre>

  If you don't have Python installed, you can download it from the official [Python website(opens in a new tab)](https://www.python.org/downloads/).

* **An IDE or Code Editor** : You'll need a code editor to work with the files. Visual Studio Code is a great choice, but you can use any editor you are comfortable with.

#### **Step 2: Create a Project Directory and Virtual Environment**

It's a best practice to keep your project dependencies isolated from your system's global Python installation. A virtual environment is perfect for this.

1. **Download and Unzip** : Download the project's starter code and unzip it into a folder on your computer.
2. **Open a Terminal** : Navigate into the project folder using your terminal or command prompt. Your terminal's path should look something like this: `.../path/to/your/FS-Agentic-AI-C4-Project/`.
3. **Create the Virtual Environment** : Run the following command to create a new virtual environment named `.venv` inside your project directory.

<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f"><div class="css-1wj0762"></div><div><code class="language-bash"><span>python -m venv .venv</span></code></div></div></pre>

1. **Activate the Virtual Environment** : You need to "activate" the environment before you can use it.

* **On macOS and Linux** :
  `<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f">``<div class="css-1wj0762"></div>``<div><code class="language-bash">``<span class="token">`source`<span>` .venv/bin/activate`</code></div>``</div></pre>`
* **On Windows** :
  `<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f">``<div class="css-1wj0762"></div>``<div><code class="language-bash">``<span>`.venv`<span class="token">`\</span>`<span>`Scripts`<span class="token">`\</span>`<span>`activate`</code></div>``</div></pre>`

   Once activated, you will see `(.venv)` at the beginning of your terminal prompt. This shows that the virtual environment is active.

#### **Step 3: Install Project Dependencies**

All the Python packages required for this project are listed in the `pyproject.toml` file.

1. **Install Packages** : With your virtual environment still active, run the following command to install all the necessary packages using `pip`.

<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f"><div class="css-1wj0762"></div><div><code class="language-bash"><span>pip </span><span class="token">install</span><span></span><span class="token">".[dev]"</span></code></div></div></pre>

   This command tells `pip` to look at the `pyproject.toml` file and install everything listed under dependencies, including the optional development packages.

#### **Step 4: Set Up Your Environment Variables**

The project needs an API key to communicate with the language model service. You should never hard-code secrets like this directly in your code. Instead, we'll use an environment variable.

1. **Create a `.env` file** : In the root directory of your project, create a new file and name it `.env`.
2. **Add Your API Key** : Open the `.env` file and add your OpenAI API key in the following format:

<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f"><div class="css-1wj0762"></div><div><code class="language-javascript"><span class="token">OPENAI_API_KEY</span><span class="token">=</span><span class="token">'your_api_key_here'</span></code></div></div></pre>

   Replace `'your_api_key_here'` with your actual API key. The `config.py` file is already set up to read this key from the `.env` file automatically.

    **Important** : The `.env` file is included in the `.gitignore` file, so it will not be committed to version control. This is a security measure to protect your key.

#### **Step 5: Generate Sample Data and Run the Project**

Now that everything is set up, you are ready to run the project.

1. **Generate SWIFT Messages** : First, run the script to create the sample SWIFT message data that your agents will process.

<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f"><div class="css-1wj0762"></div><div><code class="language-bash"><span>python generate_swift_messages.py</span></code></div></div></pre>

   This will create a `swift_messages.csv` file in the `data` directory.

1. **Run the Main Application** : Execute the main script to start the agentic workflow.

<pre class="css-0"><div data-defines-codeblock="true" tabindex="0" class="css-ift61f"><div class="css-1wj0762"></div><div><code class="language-bash"><span>python main.py</span></code></div></div></pre>

You're all set! Your local environment is now configured, and you can start working on the `TODO` items in the starter code. Happy building!

---
