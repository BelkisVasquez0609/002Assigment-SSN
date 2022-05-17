# SSN (Social Security Number) Validator
Belkis Yazmin Vasquez 1085273 
## Requirements
- **Req-1:**: When starting the system, a welcome message should be displayed on the screen.
- **Req-2:** The system should request to press enter after presenting the welcome message.
- **Req-3:** The system must request the entry of 9 digits.
- **Req-4:** The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
- **Req-5:** The second part should have 2 digits and it should be from 01 to 99.
- **Req-6:** The third part should have 4 digits and it should be from 0001 to 9999.
- **Req-7:** The system must validate that the empty data entry field is not sent.

## Criteria of acceptance
- **Cri-1-1:** The system should display a welcome message.
- **Cri-2-1:** After the welcome message, the system must request to press enter and clear the screen.
- **Cri-2-2:** The system must stabilize while waiting for the acceptance criterion number : Cri-2-1 to start the data entry process.
- **Cri-3-1:** The system must validate that the user enters 9 digits.
- **Cri-4-1:** The system must validate that the first part contains only 3 digits that are not 000,666 or some number between 900 and 999.
- **Cri-5-1:** The system must validate that the second part of the code is a number between 01 and 99.
- **Cri-6-1:** The system must validate that the third part of the code contains 4 digits and is between the range of 0001 and 9999.
- **Cri-7-1:** The system must validate that the empty data entry field is not sent.
## Test Plan

- **TC-01 The user enters a number greater or less than 9**
    - **Expected result:** The system displays the message: **Value out of range**
- **TC-02 The user leaves the data entry field empty**
    -  **Expected result:** The system displays the message: **You must complete the data entry field**
- **TC-03 The user enters another character that is not the hyphen (-)**
    -  **Expected result:** The system displays the message: **You must provide the hyphen (-) separator to be valid**
- **TC-04 The user places the numbers together**
    - **Expected result:** Debe proporcionar un separador
- **TC-05 The user user enters the combination 000, 666 or between 900 and 999 in the first 3 digits.**
    - **Expected result:** **invalid combination**

- **Positive Scenarios**

1. **023-02-4858 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
2. **402-15-2022 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
3. **322-08-3454 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
4. **320-10-1020 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
5. **800-23-3492 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
6. **750-42-9434 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
7. **230-20-2020 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
8. **325-93-4300 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
9. **783-90-1000 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers
10. **120-03-2202 ->** Nine-digit number, separated by hyphens (-), within the range of valid numbers  

- **Negative Scenarios**

12. **000-32-2010 ->** Error, contains 000 in the first 3 digits
13. **022-00-4343 ->** Error, contains 00 in the second number of the serialization
14. **012-03-0000 ->** Error, contains 0000 in the last four digits.
15. **900-02-3203 ->** Error, contains 900 in the first 3 digits
16. **999-04-3234 ->** Error, contains 999 in the first 3 digits
17. **955-03-2343 ->** Error, contains 955 in the first 3 digits
18. **666-83-9392 ->** Error, contains 666 in the first 3 digits
19. **975-23-2342 ->** Error, contains 975 in the first 3 digits
20. **925-98-9234 ->** Error, contains 925 in the first 3 digits
21. **985-03-2345 ->** Error, contains 985 in the first 3 digits
