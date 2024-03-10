import sys
import re
import requests
import argparse
from urllib.parse import quote
from bs4 import BeautifulSoup


def sslquerySearch(domainname):
    queryurl = 'https://www.shodan.io/search/facet?query=ssl:%22*.' + domainname + '%22&facet=ip'
    response = requests.get(url=queryurl).text
    soup = BeautifulSoup(response, 'lxml')
    ipaddr = []
    for ip in soup.find_all('strong'):
        ipaddr.append(ip.get_text())
    return ipaddr


def orgquerySearch(orgname):
    queryurl = 'https://www.shodan.io/search/facet?query=org:"' + orgname + '"&facet=ip'
    response = requests.get(url=queryurl).text
    soup = BeautifulSoup(response, 'lxml')
    ipaddr = []
    for ip in soup.find_all('strong'):
        ipaddr.append(ip.get_text())
    return ipaddr


def hostquerySearch(orgname):
    queryurl = 'https://www.shodan.io/search/facet?query=hostname:"' + orgname + '"&facet=ip'
    response = requests.get(url=queryurl).text
    soup = BeautifulSoup(response, 'lxml')
    ipaddr = []
    for ip in soup.find_all('strong'):
        ipaddr.append(ip.get_text())
    return ipaddr


def customquerySearch(customquery):
    queryurl = 'https://www.shodan.io/search/facet'
    payload = {'query': customquery, 'facet': 'ip'}
    response = requests.get(url=queryurl, params=payload).text
    soup = BeautifulSoup(response, 'lxml')
    ipaddr = []
    for ip in soup.find_all('strong'):
        ipaddr.append(ip.get_text())
    return ipaddr


def saveOutput(ips, outputfilename):
    f = open(outputfilename, "w")
    for ip in ips:
        f.write(ip + '\n')
    f.close


def interactiveMode():
    while True:
        print("Select Option:")
        print("1. Search By SSL Cert")
        print("2. Search By Organization Name")
        print("3. Enter Custom Query")
        print("4. Exit")
        choice = input("\n> Enter your choice: ")

        if choice == '1':
            domainname = input("> Please Enter Domain Name (eg: tesla.com): ")
            outputfilename = input("> Please enter name of the file you want output to be saved at : ")
            if re.match(r'^\s*\d*\s*$', domainname):
                print("\n> Domain name field cannot be number or blank. Please Try Again")
                continue
            elif re.match(r'^\s*\d*\s*$', outputfilename):
                print("\n> Output file name field cannot be number or blank. Please Try Again")
                continue
            else:
                print(f'\n>> Executing query: ssl:"*.{domainname}"')
                response = sslquerySearch(domainname)
                print(f'>> Saving output to "{outputfilename}" file')
                saveOutput(response, outputfilename)
                print("\n>> %d IP found and saved into '%s' file \n" % (len(response), outputfilename))

        elif choice == '2':
            orgname = input("> Please Enter Organization Name : ")
            outputfilename = input("> Please enter name of the file you want output to be saved at : ")
            if re.match(r'^\s*\d*\s*$', orgname):
                print("\n> Organization name field cannot be number or blank. Please Try Again")
                continue
            elif re.match(r'^\s*\d*\s*$', outputfilename):
                print("\n> Output file name field cannot be number or blank. Please Try Again")
                continue
            else:
                print(f'\n>> Executing query: org:"{orgname}"')
                encodedorgname = quote(orgname)
                response = orgquerySearch(encodedorgname)
                print(f'>> Saving output to "{outputfilename}" file')
                saveOutput(response, outputfilename)
                print("\n>> %d IP found and saved into '%s' file \n" % (len(response), outputfilename))

        elif choice == '3':
            query = input("> Enter Your Custom Shodan Search Query : ")
            outputfilename = input("> Please enter name of the file you want output to be saved at : ")
            if re.match(r'^\s*\d*\s*$', query):
                print("\n> Custom query field cannot be number or blank. Please Try Again")
                continue
            elif re.match(r'^\s*\d*\s*$', outputfilename):
                print("\n> Output file name field cannot be number or blank. Please Try Again")
                continue
            else:
                print(f'\n>> Executing query: {query}')
                response = customquerySearch(query)
                print(f'>> Saving output to "{outputfilename}" file')
                saveOutput(response, outputfilename)
                print(">> %d IP found and saved into '%s' file \n" % (len(response), outputfilename))

        elif choice == '4':
            break

        else:
            print("\n >> [ERROR] Invalid option selected")


def arguments():
    parser = argparse.ArgumentParser(description='This tool has two modes \n 1. Interactive Mode \n 2. Command Line Mode')
    parser.add_argument('-I', '--interactive', help='Run in Interactive Mode', action='store_true')
    parser.add_argument('-S', '--ssl', metavar='', type=str, help='Parse a Domain Name [Query : ssl:*.example.tld]')
    parser.add_argument('-O', '--org', metavar='', type=str, help='Parse an Organization Name [Query : org:org_name]')
    parser.add_argument('-H', '--host', metavar='', type=str, help='Parse a Hostname [Query : hostname:example.tld]')
    parser.add_argument('-C', '--custom', metavar='', type=str, help='Parse your custom shodan search query [Query : Custom Query]')
    parser.add_argument('-o', '--out', metavar='', type=str, help='Specify Output File Name')
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
    else:
        if args.interactive:
            interactiveMode()
        elif args.ssl:
            response = sslquerySearch(args.ssl)
            if args.out:
                saveOutput(response, args.out)
                print("Total number of IP Address Found : " + str(len(response)))
            else:
                print("\n".join(response))
                print("Total number of IP Address Found : " + str(len(response)))
        elif args.org:
            response = orgquerySearch(args.org)
            if args.out:
                saveOutput(response, args.out)
                print("Total number of IP Address Found : " + str(len(response)))
            else:
                print("\n".join(response))
                print("Total number of IP Address Found : " + str(len(response)))
        elif args.host:
            response = hostquerySearch(args.host)
            if args.out:
                saveOutput(response, args.out)
                print("Total number of IP Address Found : " + str(len(response)))
            else:
                print("\n".join(response))
                print("Total number of IP Address Found : " + str(len(response)))
        elif args.custom:
            response = customquerySearch(args.custom)
            if args.out:
                saveOutput(response, args.out)
                print("Total number of IP Address Found : " + str(len(response)))
            else:
                print("\n".join(response))
                print("Total number of IP Address Found : " + str(len(response)))


def main():
    text = '''
███████╗██████╗░███████╗███████╗██████╗░░█████╗░███╗░░██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║
█████╗░░██████╔╝█████╗░░█████╗░░██║░░██║███████║██╔██╗██║
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░██║██╔══██║██║╚████║
██║░░░░░██║░░██║███████╗███████╗██████╔╝██║░░██║██║░╚███║
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝v1.0\n'''
    print(text)
    arguments()


if __name__ == "__main__":
    main()
