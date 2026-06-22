# Quick-Fuzzer

A simple directory and subdomain fuzzer. Often times CTF platforms use directories and subdomains that are commonly found in these wordlists. This tool provides an easy way to enumerate without having to constantly check back in and load another wordlist.

### Features:
- directory fuzzing
- subdomain fuzzing
- redirect handling

### Installation and setup:
```
git clone https://github.com/rstap1/Quick-Fuzzer.git
cd Quick-Fuzzer
pip install -r requirements.txt
```
### Usage
`python3 quickfuzz.py`
(all target information is gathered after running the script)

### To come
- Threading/concurrency for increased speeds
- recursive fuzzing
- https support

Only for use on sysytems you are explicitly authorized to test.

Wordlists provided by SecLists, created by Daniel Miessler and contributors.
