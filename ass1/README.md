# Cloud Application Development Assignment 1 - Sample Answers

## Exercise 1: Setting Up Google Cloud SDK

**Q: How did you log in to your Google account using the command line?**  
A: I used the command `gcloud auth login`. This opened a browser window where I could select my Google account and grant permissions to the Google Cloud SDK.

**Q: What command did you use to set your default project?**  
A: I used `gcloud config set project [PROJECT_ID]`, replacing `[PROJECT_ID]` with the actual ID of my project.

**Q: What kind of info does `gcloud info` show you?**  
A: `gcloud info` displays various details about your Google Cloud SDK installation and configuration, including:
- Account information
- Current project
- Installed components
- Active configuration name
- Cloud SDK version
- Python version
- System PATH
- Operating system details

---

## Exercise 2: Exploring Cloud Shell

**Q: Where does Cloud Shell put you when you first open it?**  
A: Cloud Shell typically starts in your home directory, which is usually `/home/[USERNAME]`.

**Q: What are some cool tools that come pre-installed in Cloud Shell?**  
A: Cloud Shell comes pre-installed with many useful tools, including:
- `gcloud` (Google Cloud SDK)
- `gsutil` (for Google Cloud Storage)
- `kubectl` (for Kubernetes)
- `docker`
- `git`
- `vim`, `emacs`, `nano` (text editors)
- Python, Node.js, Go, Java, and other programming languages

**Q: How do you open up the code editor in Cloud Shell?**  
A: You can open the code editor by clicking on the pencil icon in the Cloud Shell toolbar, or by typing `cloudshell edit [FILENAME]` in the terminal.

---

## Exercise 3: Managing Projects with Google Cloud SDK

**Q: What's the command to list all your projects?**  
A: The command is `gcloud projects list`.

**Q: How do you make a project your default one?**  
A: Use the command `gcloud config set project [PROJECT_ID]`.

**Q: How can you see all the details about a project?**  
A: Use the command `gcloud projects describe [PROJECT_ID]`.

---

## Exercise 5: Automating Tasks with Shell Scripts in Cloud Shell

**Q: What's the command to make a script executable?**  
A: The command is `chmod +x [SCRIPT_NAME]`.  
For example: `chmod +x setup.sh`.

**Q: How did you check that your script worked correctly?**  
A: I ran the script using `./setup.sh` and then manually verified that:
- The new directory was created.
- The text file was created with the correct content.
- The Google Cloud configuration was set correctly (e.g., by running `gcloud config list`).

**Q: What tasks did your script automate?**  
A: My script automated the following tasks:
- Created a new directory.
- Created a simple text file with some content.
- Set a default Google Cloud project.

### Example Script:
```bash
#!/bin/bash

# Create a new directory
mkdir -p ~/gcp-project

# Create a simple text file
echo "This is my GCP project" > ~/gcp-project/README.txt

# Set default Google Cloud project
gcloud config set project my-project-id

echo "Setup complete!"

## Exercise 4: Using Cloud Shell for Basic Operations

**Q: What commands did you use to make your folder structure?**  
A: I used the following commands:
```bash
mkdir -p myproject/src myproject/tests myproject/docs
