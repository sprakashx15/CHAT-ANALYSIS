# Chat Analyzer

## Overview

The **Chat Analyzer** is a tool that analyzes chat conversations to generate insightful statistics and metrics. It tracks user activity, identifies the most frequently used words, and provides a visual representation of message distributions across participants. This project is useful for understanding chat dynamics, identifying active users, and highlighting common themes or topics discussed in the chat.

---

## Table of Contents

1. [Project Description](#project-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features)
5. [Data Format](#data-format)
6. [Results and Output](#results-and-output)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Description

The **Chat Analyzer** processes a chat conversation to provide the following insights:

- **Message Count by User:** Tracks the number of messages sent by each participant.
- **Most Used Words:** Analyzes the most frequent words in the chat, offering a glimpse into the main topics of discussion.
- **Message Distribution:** Visualizes how messages are distributed across users and over time, highlighting active periods or participants.

This tool can be applied to group chats, forums, or any other form of text-based communication.

---

## Installation

To set up and run this project, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/chat-analyzer.git
```

2. Navigate to the project directory:

```bash
cd chat-analyzer
```

3. Install the required dependencies using **pip**:

```bash
pip install -r requirements.txt
```

---

## Usage

Once you have installed the necessary dependencies, you can run the **Chat Analyzer** on a chat log file. To do so, run the following Python script:

```bash
python chat_analyzer.py --chat_file 'data/chat_log.txt'
```

This command will analyze the chat log and output various statistics, including message counts, most frequent words, and message distribution.

### Example Command:

```bash
python chat_analyzer.py --chat_file 'data/chat_log.txt' --output 'results/stats_output.csv'
```

---

## Features

- **Message Count by User:** A summary of how many messages each user has sent during the conversation.
- **Most Used Words:** Identifies the most common words or phrases used in the chat, helping to highlight trending topics.
- **Message Distribution Over Time:** A visualization of when messages were sent, allowing you to see active periods or changes in conversation dynamics.
- **User Activity Visualization:** Graphically shows how many messages each user has sent throughout the chat session.

---

## Data Format

The tool requires the chat log in a text format with the following structure:

```
[Timestamp] [User]: [Message]
```

For example:

```
2025-03-23 10:00:00 John: Hey, how's it going?
2025-03-23 10:02:15 Alice: Good, just working on the project.
2025-03-23 10:05:30 John: Cool, I just finished my part.
```

Ensure that the chat log is formatted properly before feeding it into the tool.

---

## Results and Output

The tool will generate several statistics and outputs:

1. **Message Count by User** – A list of users with the number of messages they've sent.
2. **Most Used Words** – A list of the most frequently used words in the chat, possibly with a frequency count.
3. **Message Distribution** – A graphical plot showing message activity over time and the distribution across users.

These results will be displayed on the console or saved in the specified output file (e.g., CSV, or graphical format).

---

## Contributing

We welcome contributions to this project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the changes to your forked repository (`git push origin feature-branch`).
5. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you need any changes or additional sections!