# Freedan - Shodan IP Extractor

Freedan is a Python tool designed to streamline reconnaissance efforts during bug bounty programs and penetration testing activities. This tool leverages Shodan's capabilities to extract IP addresses based on various dorks or search queries using Shodan facet. Notably, Freedan operates without requiring an active subscription or user login, providing users with the ability to extract over 1000+ IP addresses, surpassing the limitations imposed by Shodan for non-subscribers.

## Features
- Extracts IP addresses from Shodan using different dorks or search queries.
- Utilizes Shodan facet for efficient data extraction.
- No active subscription or login required, offering unrestricted access to reconnaissance capabilities.
- Enables the extraction upto 1000 IP addresses, surpassing the limitations imposed by Shodan for non-subscribers.

## Installation

**To use Freedan, follow these steps:**

1. Clone the repository:

   ```bash
   git clone https://github.com/niteshmmgupta/freedan.git && cd freedan/
   ```
2. Install dependencies using pip:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

#### Freedan provides two modes for user convenience:

1. **Interactive Mode**
    
    - To run Freedan in interactive mode, use the following command:

        ```bash
        python3 freedan.py -I
        ```

2. **CommandLine Mode**

    - To see the help menu for command line mode, use the following command:

        ```bash
        python3 freedan.py -h
        ```

    - In commandline mode user will directly see valie in terminal itself if `-o`

    - **Help Menu**
        ```
        ███████╗██████╗░███████╗███████╗██████╗░░█████╗░███╗░░██╗
        ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║
        █████╗░░██████╔╝█████╗░░█████╗░░██║░░██║███████║██╔██╗██║
        ██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░██║██╔══██║██║╚████║
        ██║░░░░░██║░░██║███████╗███████╗██████╔╝██║░░██║██║░╚███║
        ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝v1.0
        usage: freedan.py [-h] [-I] [-S] [-O] [-H] [-C] [-o]

        This tool has two modes 1. Interactive Mode 2. Command Line Mode

        options:
        -h, --help         show this help message and exit
        -I, --interactive  Run in Interactive Mode
        -S , --ssl         Parse a Domain Name [Query : ssl:*.example.tld]
        -O , --org         Parse an Organization Name [Query : org:org_name]
        -H , --host        Parse a Hostname [Query : hostname:example.tld]
        -C , --custom      Parse your custom shodan search query [Query : Custom Query]
        -o , --out         Specify Output File Name
        ```

    - **Command Examples**
        ```
        python3 freedan.py -S tesla.com -o outputfile.txt
        ```
        ```
        python3 freedan.py -O "Tesla Motors" -o outputfile.txt
        ```
        ```
        python3 freedan.py -C 'ssl.cert.subject.cn:tesla.com' -o outputfile.txt
        ```
    
    - If `-o` output file name is not provided the output will be printed in terminal itself. 

</br>**Note**</br>
Please note that Freedan is my first tool. While I've put effort into ensuring its functionality, there may be some issues. I am open to any constructive suggestions or contributions to enhance and refine the tool. Your feedback is valued, and I encourage users to utilize Freedan responsibly.

</br>**Disclaimer:**</br>

This tool is designed to provide an accessible resource for beginners who may not have the means to subscribe to Shodan's premium services. It utilizes Shodan facets to gather publicly available data that is already shared by Shodan. It is essential to note the following:

- Limited Scope: This tool fetches data within the limitations of Shodan facets and does not access any information beyond what is publicly available.
- Encouragement for Shodan Subscription: Users who can afford a Shodan subscription are encouraged to explore the full range of features and benefits that come with it. A Shodan subscription offers a more comprehensive and in-depth experience.
- Legal and Ethical Use: Users are responsible for ensuring the legal and ethical use of this tool. It is crucial to comply with all applicable laws and regulations while using the tool.