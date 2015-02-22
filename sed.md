## sed usage

### Combination with find
Apply sed to files found by the find command:
```bash
$ find path/to/specify -iname \*.txt -exec sed -e "s#old_pattern#new_pattern#g" {} -i-old \;
```
Note the  usage of option  -i-old which keeps  a backup of  the modified
file (e.g., test.txt -> test.txt-old).

You may  also want to apply  a cautious strategy (by  replacing -exec with
-ok):
```bash
$ find path/to/specify -iname \*.txt -ok sed -e "s#old_pattern#new_pattern#g" {} -i-old \;
```
