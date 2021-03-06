# CloudECG_jsy
# HRM with web service

## HW Assignment #3

Medical Software Design Evaluators: Palmeri, Kumar, Desai

Contributors: Hoballah, S. Shah, Saxena

Travis CI Build Status
---

[![Build Status](https://travis-ci.org/ss842/CloudECG_jsy.svg?branch=master)](https://travis-ci.org/ss842/CloudECG_jsy)

License
---

MIT License Copyright (c) [2017] [J. Hoballah, Y. Saxena, S. Shah]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Running the Code:
---

Sending time and voltage json dictionaries to:

1) vcm-1828.vm.duke.edu:5000/api/heart_rate/summary will return a summary of instant heart rates, tachy- and brachycardia annotations across all time points

2) vcm-1828.vm.duke.edu:5000/api/heart_rate/average will return a summary of average heart rates, tachy- and brachycardia annotations across time intervals

3) vcm-1828.vm.duke.edu:5000/api/requests will return total number of requests to our service to date

