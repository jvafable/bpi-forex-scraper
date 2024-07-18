# BPI Forex Scraper

Tracking BPI's indicative foreign exchange rates at https://www.bpi.com.ph/personal/bank/forex/rates.

This repository scrapes the BPI exchange rates page every 20 minutes and saves it in `bpi-forex-rates.json`. Any changes in rates will be visible in the commit diff.


This scraping technique was taken from https://simonwillison.net/2020/Oct/9/git-scraping/.