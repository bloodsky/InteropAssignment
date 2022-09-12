# InteropAssignment

Simple terminal application written in Python, with numbered menu for working with CSV files. <br />
Folder ```input-test-files``` contains 3 csv test files.<br />
After cloning the repository just cd inside project directory and

```bash
  python3 main.py
```

The management of missing values takes place following the constraints indicated by the specification. 
An ID field must always be present, unique and not negative. On the contrary, since no constraint regarding 
the yearly-amount field is indicated in the specification, and having empty entries related to this, a yearly 
amount field is implemented as an optional which when not present is assumed as zero. the same 
goes for monthly variation.

the test files to perform the assignments are located in the folder: 
```input-test-files``` <br />
The two files referred to as 
```input_file_test1.csv``` 
```input_file_test2.csv``` <br />
they are example files with errors, as reported by the specification. 
```clean_input_test.csv``` is the clean file meaning that is an error-free csv file.