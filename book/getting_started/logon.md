# Logging on

Once you have an account you'll be able to connect to the University HPC systems using a secure shell (SSH). In the page below we'll cover how to make sure you can SSH from your machine (installing any prerequired software) and how to configure your SSH to connect from off-campus.

## Connecting from Linux/MacOS systems

### SSH via Terminal

Linux and MacOS systems all come with a Terminal application that opens a command-line shell. In the following example code snippets we'll be connecting with the username `exuser`. When you come to log in to a system you'll need to use your own university username in place of `exuser`.

To log in from your Terminal use the following command:

```bash
# to log into ARC4
$ ssh exuser@arc4.leeds.ac.uk

# to log into ARC4
$ ssh exuser@arc3.leeds.ac.uk
```

You will then be prompted for your password which you should enter.

```{note} For security placeholder characters
will not appear as you type your password. Your keystrokes are recorded so please type carefully!
```

### Graphics forwarding (X11)

Secure shell allows X display (GUI) traffic to be tunnelled (and encrypted) through the SSH connection. Provided your local display is set up correctly, the -Y flag can be used to allow trusted X11 forwarding:

```bash
$ ssh -Y exuser@arc4.leeds.ac.uk
```

```{note} **For macOS Users**
The latest versions of macOS do not have an X11 client installed so this will need to be downloaded and installed seperately. X11 for Mac can be obtained from the [XQuartz](http://www.xquartz.org/index.html). This is a dmg file so will prompt you with the correct instructions for installation.
```

## Connecting from Windows

Windows by default does not come with an SSH client. Therefore, we need to install an SSH client and an X server for forwarding graphical applications. We recommend using [MobaXTerm](http://mobaxterm.mobatek.net/) which combines an SSH program (similar to PuTTY), a simple file transfer utility, a text editor and an X-Server into a single package.

### Setting up MobaXTerm

To get started you need to install MobaXTerm. You can do this by downloading the **Portable Home edition** [(Click here to go to the download page)](https://mobaxterm.mobatek.net/download-home-edition.html) which is a .zip file containing the software. You can follow the steps in the below video to help walkthrough getting set up. 

<iframe src="https://mymedia.leeds.ac.uk/Mediasite/Play/7c25b8af4c7f43f7898efeba0ec6dd311d" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" scrolling="auto" allowfullscreen="allowfullscreen" style="display:block;"> </iframe> 


## Connecting from off-campus

