# Useful Commands
A collection of commands helpful when working with RIAPS

## Terminal Controls (Linux)
- Open new terminal window: `Ctrl + Alt + T`
- Open new tab in current terminal window: `Ctrl + Shift + T`
## Generally useful commands on the VM
### Editing files with `nano <filename>`
- Save file: `Ctrl + O`
- Exit: `Ctrl + x`
  - If you have unsaved changes, it will ask you to confirm the filename; just hit `Enter` to continue
  - If you get "Permission denied", you need to edit the file with root privileges. (`sudo nano`...)


### Navigation
Print out current location
```bash
pwd
```  
List files/directories in current location
```bash
ls
```  
Move down into subdirectory
```bash
cd <directory name>
``` 
Move up into parent directory
```bash
cd ..
```  
### Working with files
Create new blank file
```bash
touch <new file name>
```  
Copy file into new location (within same computer)
```bash
cp <file to be moved> <new file location> <directory name>
```  
Delete file
```bash
rm <file name>
```
Delete directory
```bash
rm -r <directory name>
```
# Useful commands for the BeagleBone Black (BBB)
## From the VM
"Remote in" to a BBB
```bash
ssh <riaps-abcd.local or IP address>
```


## When remotely logged in to the BBB
View the riaps-deplo logs (and any duly configured apps)
```bash
journalctl -u riaps-deplo.service -f
```

Set time/date, (add 4 hours to make UTC time)
```bash
sudo timedatectl set-ntp 0
sudo timedatectl set-time "2023-05-16 12:50:00"
```
Fully removing RIAPS processes and code on a node
```bash
sudo systemctl stop riaps-deplo.service
pgrep -l riaps_
# Note all PIDs (integers) that were running 
sudo kill -9 <PID> # Run for each riaps_ PID that was returned before
sudo rm -rf /home/riaps/riaps_apps/* # delete all deployed RIAPS code
sudo systemctl restart riaps-deplo.service
```
# Using `tmux` to view logs
Launch RIAPS log viewer with the tmux driver
```bash
riaps_logger --app -d tmux
```
List currently active `tmux` sessions
```
tmux ls
```
Attach a terminal to the `tmux` session
```bash
tmux attach -t app
```
## `tmux` commands  
>`tmux` commands work by **first** sending a "prefix", which is `Ctrl + b` by default. Most commands work by sending the prefix, releasing, then hitting the next key. Some, such as resizing panes, require holding down the prefix while tapping the commanding key

|Command | Key |
| --- | --- |
Switch current pane | `<arrow key>`  
Resize current pane (HOLD PREFIX) |  `<arrow key>`
Kill current pane | `x` (will ask to confirm, `y/n`)  
Re-arrange all panes | `spacebar`  
View all `tmux` commands | `?`
