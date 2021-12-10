# Logging on

```{warning} **Read carefully**
This is a big article that covers lots of important details about logging in especially for those connecting from off campus.
```

Once you have an account you'll be able to connect to the University HPC systems using a secure shell (SSH). In the page below we'll cover how to make sure you can SSH from your machine (installing any prerequired software) and how to configure your SSH to connect from off-campus.

## Setup

Before you can begin connecting to the University HPC systems you'll need to complete the following setup:

- Have requested and had confirmation that your HPC account has been created. You out more on our [Requesting a HPC Account page](./request_hpc_acct)
- Have an SSH client installed on your device. See below for different details depending on your operating system ([MacOS/Linux](#macos-linux-terminal) or [Windows](#installing-mobaxterm))

### MacOS/Linux Terminal

If you are a MacOS or Linux user you will probably have an SSH client already installed that can be used via the Terminal application on your device.

Open the Terminal application and you're ready to to connect. Next you'll need to read more about [Connecting on campus](#Connecting-on-campus) or [Connecting from off campus](#Connecting-from-off-campus) depending on your circumstances.

### Installing MobaXTerm

To get started you need to install MobaXTerm. You can do this by downloading the **Portable Home edition** [(Click here to go to the download page)](https://mobaxterm.mobatek.net/download-home-edition.html) which is a .zip file containing the software. You can follow the steps in the below video to help walkthrough getting set up.

<iframe src="https://mymedia.leeds.ac.uk/Mediasite/Play/7c25b8af4c7f43f7898efeba0ec6dd311d" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" scrolling="auto" allowfullscreen="allowfullscreen" style="display:block;"> </iframe>

## Connecting on campus

### SSH via Terminal app (MacOS/Linux)

Linux and MacOS systems all come with a Terminal application that opens a command-line shell. In the following example code snippets we'll be connecting with the username `exuser`. When you come to log in to a system you'll need to use your own university username in place of `exuser`.

To log in from your Terminal use the following command:

```bash
# to log into ARC4
$ ssh exuser@arc4

# to log into ARC3
$ ssh exuser@arc3
```

The first time you SSH to either ARC4 or ARC3 you will be prompted to confirm the fingerprint of the host you're connecting to. You can check the unique fingerprints for ARC3 and ARC4 in the [fingerprint details](#fingerprint-details) below.

```
The authenticity of host 'arc4 (129.11.26.163)' can't be established.
ECDSA key fingerprint is SHA256:lPkw/7SrBqqQkS7lUm+tBN9JIGX9B8Gw7FdkK3MrpLM.
ECDSA key fingerprint is MD5:4f:d8:bc:ad:16:8b:ab:54:cf:29:04:c7:cc:20:5b:fc.
Are you sure you want to continue connecting (yes/no)?
```

ARC3:

```
The authenticity of host 'arc3 (129.11.26.153)' can't be established.
ECDSA key fingerprint is SHA256:cOA3zaJLawry0uVQ3VPveyxcrUJ+/8hRcr59xSbYRNI.
ECDSA key fingerprint is MD5:c2:b1:9a:c1:44:aa:ba:a1:db:c6:b7:d4:48:9d:74:89.
Are you sure you want to continue connecting (yes/no)?
```

You should confirm the key fingerprints match from fingerprints shown in the [fingerprint details](#fingerprint-details) section and type `yes` and press Enter to proceed.
If the keys do not match do **not** continue and contact Research Computing immediately via [https://bit.ly/arc-help](https://bit.ly/arc-help)

You will then be prompted for your password.

```bash
$ ssh exuser@arc4
exuser@arc4's password:
```

If you type your password incorrectly you will get a `Permission denied, please try again` message.
If this happens re-enter your password but be extra careful!

```{note} For security placeholder characters (like an asterisk)
will not appear as you type your password. Your keystrokes are recorded so please type carefully!
```

### Connecting with MobaXTerm

```{warning}
**As of July 2021 the University is using 2-factor authentication for password-based access to remote-access.**
You will need to make sure you have [enrolled with Duo with your University account](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014659) and will be required to [use Duo to authenticate](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014641) after submitting your password to remote-access.
```

Once you have MobaXTerm downloaded you can connect to ARC via two mechanisms: using the builtin local terminal to connect using SSH commands; or creating an [SSH session via the GUI](#creating-an-ssh-session).

#### Creating an SSH session

You can create an SSH session to connect to ARC using the following steps:

| 1. Open the initial MobaXTerm Menu and select Session                                     |
| ----------------------------------------------------------------------------------------- |
| ![Open the initial MobaXTerm Menu and select Session](../assets/img/logon/mobaXTerm1.png) |

| 2. In the Session Wizard Window select SSH                                     |
| ------------------------------------------------------------------------------ |
| ![In the Session Wizard Window select SSH](../assets/img/logon/mobaXTerm2.png) |

| 3. Input the basic setting details for SSH session: the host (address of ARC), the username (your university username)                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Input the basic setting details for SSH session: the host (address of ARC), the username (your university username)](../assets/img/logon/mobaXTerm3.png) |

| 4. Select the Network Settings tab within the Session Settings window                                     |
| --------------------------------------------------------------------------------------------------------- |
| ![Select the Network Settings tab within the Session Settings window](../assets/img/logon/mobaXTerm4.png) |

| 5. Click on the large button labelled "SSH gateway (jump host)" and input details for connecting to remote-access.leeds.ac.uk (Gateway SSH server) and specify your username |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Select the "Connect through SSH gateway (jump host) option](../assets/img/logon/mobaXTerm5.png)                                                                            |

| 6. You will immediately be prompted for your password to connect to the remote-access server                                     |
| -------------------------------------------------------------------------------------------------------------------------------- |
| ![You will immediately be prompted for your password to connect to the remote-access server](../assets/img/logon/mobaXTerm6.png) |

| 7. You will immediately be prompted for to enter your [Duo two-factor code](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014641) which can be found on your Duo App |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![You will immediately be prompted for to enter your Duo two-factor login code which can be found on your Duo App](../assets/img/logon/mobaXTerm6-5.png)                          |

| 8. After it accepts your password it will request your password again, this time to log into ARC4 (This may not happen automatically and you may need to double click on session name that appears on the right hand User sessions section) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![After it accepts your password it will request your password again, this time to log into ARC4](../assets/img/logon/mobaXTerm7.png)                                                                                                       |

```{note} For security placeholder characters
will not appear as you type your password. Your keystrokes are recorded so please type carefully!
```

| 9. Once successful you will see the ARC4 message of the day and the ARC prompt                                     |
| ------------------------------------------------------------------------------------------------------------------ |
| ![Once successful you will see the ARC4 message of the day and the ARC prompt](../assets/img/logon/mobaXTerm8.png) |

| 10. You can restart an existing session after it has closed by double-clicking the session under the User sessions folder on the left-hand panel of the main MobaXTerm menu |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| ![You can restart an existing session after it has closed by double-clicking the session under the User sessions](../assets/img/logon/mobaXTerm9.png)

#### SSHing via the MobaXTerm Terminal

We can use the MobaXTerm Terminal like a standard unix shell to navigate around our local computer and also to SSH onto remote hosts including ARC.

| 1. Within a local Terminal on MobaXTerm we use the `ssh` command to connect to ARC                                    |
| --------------------------------------------------------------------------------------------------------------------- |
| ![Within a local Terminal on MobaXTerm we use the `ssh` command to connect to ARC](../assets/img/logon/mobaSSH_1.png) |

| 2. We are then prompted to submit our password to connect to `remote-access.leeds.ac.uk`                      |
| ------------------------------------------------------------------------------------------------------------- |
| ![We are then prompted to submit our password to connect to remote-access](../assets/img/logon/mobaSSH_2.png) |

| 3. We are then prompted select how to receive a Duo 2 factor authentication prompt either via the app or as a text message. Select your preferred option and either approve the push or input a passcode that is sent to you via SMS |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![We are then prompted to submit our password to connect to arc4](../assets/img/logon/mobaSSH_3.png)                                                                                                                                 |

| 3. We are then prompted to submit our password to connect to `arc4.leeds.ac.uk`                      |
| ---------------------------------------------------------------------------------------------------- |
| ![We are then prompted to submit our password to connect to arc4](../assets/img/logon/mobaSSH_4.png) |

| 4. Once we have successfully submitted our passwords our prompt will change and the message of the day for ARC4 will be displayed |
| --------------------------------------------------------------------------------------------------------------------------------- |

| ![ARC4 message of the day on MobaXTerm](../assets/img/logon/mobaSSH_5.png)

## Connecting from off campus

### Connecting from Linux/MacOS systems

```{warning}
**As of July 2021 the University is using 2-factor authentication for password-based access to remote-access.**
You will need to make sure you have [enrolled with Duo with your University account](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014659) and will be required to [use Duo to authenticate](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014641) after submitting your password to remote-access.
```

In order to connect to ARC when you're off campus you'll need to do some extra configuration so that your SSH connection goes via our `remote-access` server. The following steps outline how to setup this configuration:

1. Open a Terminal on your Linux/macOS machine
2. Create a directory called `.ssh` in your home directory (if one doesn't already exist)

   ```bash
   $ mkdir ~/.ssh
   ```

3. Then open a text editor of your choice and create a file called `config` in your `.ssh` directory

   ```bash
   # for instance use the simple nano text editor
   $ nano ~/.ssh/config
   ```

4. Within this file include the following contents where `USERNAME` is replaced by your university username

   ```
   Host *.leeds.ac.uk !remote-access.leeds.ac.uk
   ProxyJump USERNAME@remote-access.leeds.ac.uk
   User USERNAME
   ```

   ````{admonition} Old version of SSH
   If you're using an old version of OpenSSH, you may get an error: `Bad configuration option: ProxyJump`.  In this case you'll want to use this instead:

   ```
   Host *.leeds.ac.uk !remote-access.leeds.ac.uk
   ProxyCommand ssh -o PreferredAuthentications=keyboard-interactive -W %h:%p USERNAME@remote-access.leeds.ac.uk
   User USERNAME
   ```
   ````

5. Save this file and your configuration is all set up!

You should now run the normal SSH commands in the terminal specifying the host you wish to connect to.

```bash
# to connect to ARC4
$ ssh exuser@arc4.leeds.ac.uk

# to connect to ARC3
$ ssh exuser@arc3.leeds.ac.uk
```

You'll be prompted to login to remote-access.leeds.ac.uk first and may be presented with an interactive login that looks like below:

```bash
$ ssh arc4.leeds.ac.uk
Password:
```

After entering your password carefully if it is correct you will receive the Duo 2 factor authentication prompt.

```bash
$ ssh arc4.leeds.ac.uk
Password:
Duo two-factor login for exuser@leeds.ac.uk

Enter a passcode or select one of the following options:

 1. Duo Push to +XX XXXX XXXXXXX
 2. SMS passcodes to +XX XXXX XXXXXX (next code starts with: 2)

Passcode or option (1-2):
```

Enter your prefered option and authenticate using Duo and you will be prompted to enter your password for ARC4.

```bash
$ ssh arc4.leeds.ac.uk
Password:
Duo two-factor login for exuser@leeds.ac.uk

Enter a passcode or select one of the following options:

 1. Duo Push to +XX XXXX XXXXXX
 2. SMS passcodes to +XX XXXX XXXXXX (next code starts with: 2)

Passcode or option (1-2): 1
exuser@arc4.leeds.ac.uk's password:
```

Again carefully enter your password and if you've entered it correctly you'll see the ARC4 message of the day and have successfully connected.

### Connecting from Windows

Connecting from Windows requires the installation of an SSH client. We recommend and support users using MobaXTerm, please consult the [setup section](#installing-mobaxterm) about installing this application.

### Connecting via MobaXTerm

```{warning}
**As of July 2021 the University is using 2-factor authentication for password-based access to remote-access.**
You will need to make sure you have [enrolled with Duo with your University account](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014659) and will be required to [use Duo to authenticate](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014641) after submitting your password to remote-access.
```

Once you have MobaXTerm downloaded you can connect to ARC via two mechanisms: using the builtin local terminal to connect using SSH commands; or creating an [SSH session via the GUI](#creating-an-ssh-session-off-campus).

#### Creating an SSH session (off-campus)

You can create an SSH session to connect to ARC using the following steps:

| 1. Open the initial MobaXTerm Menu and select Session                                     |
| ----------------------------------------------------------------------------------------- |
| ![Open the initial MobaXTerm Menu and select Session](../assets/img/logon/mobaXTerm1.png) |

| 2. In the Session Wizard Window select SSH                                     |
| ------------------------------------------------------------------------------ |
| ![In the Session Wizard Window select SSH](../assets/img/logon/mobaXTerm2.png) |

| 3. Input the basic setting details for SSH session: the host (address of ARC), the username (your university username)                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Input the basic setting details for SSH session: the host (address of ARC), the username (your university username)](../assets/img/logon/mobaXTerm3.png) |

| 4. Select the Network Settings tab within the Session Settings window                                     |
| --------------------------------------------------------------------------------------------------------- |
| ![Select the Network Settings tab within the Session Settings window](../assets/img/logon/mobaXTerm4.png) |

| 5. Click on the large button labelled "SSH gateway (jump host)" and input details for connecting to remote-access.leeds.ac.uk (Gateway SSH server) and specify your username |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Select the "Connect through SSH gateway (jump host) option](../assets/img/logon/mobaXTerm5.png)                                                                            |

| 6. You will immediately be prompted for your password to connect to the remote-access server                                     |
| -------------------------------------------------------------------------------------------------------------------------------- |
| ![You will immediately be prompted for your password to connect to the remote-access server](../assets/img/logon/mobaXTerm6.png) |

| 7. You will immediately be prompted for to enter your [Duo two-factor code](https://it.leeds.ac.uk/it?id=kb_article&sysparm_article=KB0014641) which can be found on your Duo App |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![You will immediately be prompted for to enter your Duo two-factor login code which can be found on your Duo App](../assets/img/logon/mobaXTerm6-5.png)                          |

| 8. After it accepts your password it will request your password again, this time to log into ARC4 (This may not happen automatically and you may need to double click on session name that appears on the right hand User sessions section) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![After it accepts your password it will request your password again, this time to log into ARC4](../assets/img/logon/mobaXTerm7.png)                                                                                                       |

```{note} For security placeholder characters
will not appear as you type your password. Your keystrokes are recorded so please type carefully!
```

| 9. Once successful you will see the ARC4 message of the day and the ARC prompt                                     |
| ------------------------------------------------------------------------------------------------------------------ |
| ![Once successful you will see the ARC4 message of the day and the ARC prompt](../assets/img/logon/mobaXTerm8.png) |

| 10. You can restart an existing session after it has closed by double-clicking the session under the User sessions folder on the left-hand panel of the main MobaXTerm menu |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![You can restart an existing session after it has closed by double-clicking the session under the User sessions](../assets/img/logon/mobaXTerm9.png)                       |

#### Using the MobaXTerm Terminal

Alternatively, you can connect to ARC using the builtin Terminal within MobaXTerm and use the `ssh` command.

##### Configuring MobaXTerm Terminal

In order to successfully connect off-campus you are required to adjust some settings within MobaXTerm to create a persistent home directory and create a configuration file for SSH.

| 1. Open the initial MobaXTerm Menu and select Settings                                   |
| ---------------------------------------------------------------------------------------- |
| ![Open the initial MobaXTerm Menu and select Settings](../assets/img/logon/mobaSSH1.png) |

| 2. Select the folder icon on the right-hand side of the Persistent home directory setting box                                   |
| ------------------------------------------------------------------------------------------------------------------------------- |
| ![Select the folder icon on the right-hand side of the Persistent home directory setting box](../assets/img/logon/mobaSSH2.png) |

| 3. Select a folder location to use for your persistent home directory (this can be any writeable folder on your computer), here I am using my C:\User\university_username folder |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Select a folder location to use for your persistent home directory](../assets/img/logon/mobaSSH3.png)                                                                          |

| 4. This takes you back to the MobaXTerm Setting Menu, where you can now select OK                                   |
| ------------------------------------------------------------------------------------------------------------------- |
| ![This takes you back to the MobaXTerm Setting Menu, where you can now select OK](../assets/img/logon/mobaSSH4.png) |

| 5. You will then be prompted to restart MobaXTerm so that the new settings are applied                                   |
| ------------------------------------------------------------------------------------------------------------------------ |
| ![You will then be prompted to restart MobaXTerm so that the new settings are applied](../assets/img/logon/mobaSSH5.png) |

| 6. When MobaXTerm restarts, select the Start Local Terminal option                                   |
| ---------------------------------------------------------------------------------------------------- |
| ![When MobaXTerm restarts, select the Start Local Terminal option](../assets/img/logon/mobaSSH6.png) |

| 7. This takes you to the MobaXTerm terminal view                                   |
| ---------------------------------------------------------------------------------- |
| ![This takes you to the MobaXTerm terminal view](../assets/img/logon/mobaSSH7.png) |

| 8. Next create a folder called `.ssh` using the command `mkdir .ssh`               |
| ---------------------------------------------------------------------------------- |
| ![This takes you to the MobaXTerm terminal view](../assets/img/logon/mobaSSH8.png) |

```{note} If this folder already exists you will get an error saying this file/folder already exists just skip to step 9

```

| 9. Then go to Tools > MobaTextEditor                                               |
| ---------------------------------------------------------------------------------- |
| ![This takes you to the MobaXTerm terminal view](../assets/img/logon/mobaSSH9.png) |

| 10. Type the contents of the file as follows where `USERNAME` is your university username                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <pre id="codecell0"> Host \*.leeds.ac.uk !remote-access.leeds.ac.uk <br> ProxyJump USERNAME@remote-access.leeds.ac.uk <br> User USERNAME <br> <br> Host remote-access.leeds.ac.uk <br> PreferredAuthentications publickey,keyboard-interactive </pre> |
| ![This takes you to the MobaXTerm terminal view](../assets/img/logon/mobaSSH10.png)                                                                                                                                                                   |

| 11. Once complete go to File > Save As                                   |
| ------------------------------------------------------------------------ |
| ![Once complete go to File > Save As](../assets/img/logon/mobaSSH11.png) |

| 12. Select the `.ssh` folder you created in the step 8.                                  |
| ---------------------------------------------------------------------------------------- |
| ![ Select the .ssh folder you created in the step 8.](../assets/img/logon/mobaSSH12.png) |

| 13. Name the file as `config` and press Save and close MobaTextEditor          |
| ------------------------------------------------------------------------------ |
| ![Name the file as `config` and press Save](../assets/img/logon/mobaSSH13.png) |

And now MobaXTerm should be configured so we can SSH to ARC using the MobaXTerm Terminal.

##### SSHing via the MobaXTerm Terminal

We can use the MobaXTerm Terminal like a standard unix shell to navigate around our local computer and also to SSH onto remote hosts including ARC. In order to connect to ARC we need to make sure we have configured MobaXTerm as described in [the above section](#configuring-mobaxterm-terminal)

| 1. Within a local Terminal on MobaXTerm we use the `ssh` command to connect to ARC                                    |
| --------------------------------------------------------------------------------------------------------------------- |
| ![Within a local Terminal on MobaXTerm we use the `ssh` command to connect to ARC](../assets/img/logon/mobaSSH_1.png) |

| 2. We are then prompted to submit our password to connect to `remote-access.leeds.ac.uk`                      |
| ------------------------------------------------------------------------------------------------------------- |
| ![We are then prompted to submit our password to connect to remote-access](../assets/img/logon/mobaSSH_2.png) |

| 3. We are then prompted select how to receive a Duo 2 factor authentication prompt either via the app or as a text message. Select your preferred option and either approve the push or input a passcode that is sent to you via SMS |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ![We are then prompted to submit our password to connect to arc4](../assets/img/logon/mobaSSH_3.png)                                                                                                                                 |

| 3. We are then prompted to submit our password to connect to `arc4.leeds.ac.uk`                      |
| ---------------------------------------------------------------------------------------------------- |
| ![We are then prompted to submit our password to connect to arc4](../assets/img/logon/mobaSSH_4.png) |

| 4. Once we have successfully submitted our passwords our prompt will change and the message of the day for ARC4 will be displayed |
| --------------------------------------------------------------------------------------------------------------------------------- |
| ![ARC4 message of the day on MobaXTerm](../assets/img/logon/mobaSSH_5.png)                                                        |
| --------------------------------------------------------------------------------------------------------------------------------- |
| ![ARC4 message of the day on MobaXTerm](../assets/img/logon/mobaSSH_5.png)                                                        |

## Graphics forwarding (X11) from a Terminal

```{note}
For Windows users, graphical forwarding is automatically configured by MobaXTerm when [connecting using a session](#Creating-an-SSH-session)
```

Secure shell allows X display (GUI) traffic to be tunnelled (and encrypted) through the SSH connection. Provided your local display is set up correctly, the -Y flag can be used to allow trusted X11 forwarding:

```bash
$ ssh -Y exuser@arc4.leeds.ac.uk
```

```{note} **For macOS Users**
The latest versions of macOS do not have an X11 client installed so this will need to be downloaded and installed seperately. X11 for Mac can be obtained from the [XQuartz](http://www.xquartz.org/index.html). This is a dmg file so will prompt you with the correct instructions for installation.
```

## Fingerprint details

These are the important ssh fingerprint details for connecting to the hosts referenced in this article. On first connection to these hosts, you should verify that the fingerprint reported in your client matches one of those listed here.

```
SHA256:SZN1IZ9rL0mhpnxhVG5uxbtVFMZAISg98X9ovHlh8Fg remote-access.leeds.ac.uk (RSA)
SHA256:RoIHn1BDSlh/WjGHEG73OFISe6H3q3iLuM4z6tGu29Q remote-access.leeds.ac.uk (ECDSA)
SHA256:D2c29ZoFFDlwo0Ou/1erlSJwpI5bQQEPvarVVhShL5E remote-access.leeds.ac.uk (ED25519)
MD5:a3:ed:e5:ef:85:2f:5c:67:f4:6a:75:8a:6b:df:be:7c remote-access.leeds.ac.uk (RSA)
MD5:a2:eb:14:f3:a6:4e:af:e3:ca:b2:91:80:26:77:62:aa remote-access.leeds.ac.uk (ECDSA)
MD5:67:e4:aa:13:bf:de:7a:cb:41:1f:89:1f:56:aa:a9:c0 remote-access.leeds.ac.uk (ED25519)

SHA256:sGkFPzE909xWfNOT4nK+/RGY2kVOc7loksdUSBO6mLg arc4.leeds.ac.uk (RSA)
SHA256:lPkw/7SrBqqQkS7lUm+tBN9JIGX9B8Gw7FdkK3MrpLM arc4.leeds.ac.uk (ECDSA)
SHA256:BkElel9biuGN/k+bKh6u6GJ6rmbHo8bQxzUwTpjkr1w arc4.leeds.ac.uk (ED25519)
MD5:e0:3d:65:ec:36:43:a0:e8:71:39:ea:49:a6:17:6b:c1 arc4.leeds.ac.uk (RSA)
MD5:4f:d8:bc:ad:16:8b:ab:54:cf:29:04:c7:cc:20:5b:fc arc4.leeds.ac.uk (ECDSA)
MD5:27:2f:a4:fe:e3:91:af:5c:a5:54:5a:11:55:7f:ad:61 arc4.leeds.ac.uk (ED25519)

SHA256:lSrebEoCB31fZzKPlw2jO05P7bNi0ewUQPD/I9+0Ntg arc3.leeds.ac.uk (RSA)
SHA256:cOA3zaJLawry0uVQ3VPveyxcrUJ+/8hRcr59xSbYRNI arc3.leeds.ac.uk (ECDSA)
SHA256:qOUEf22sKATCVhcVDTJTt++Rihwo/QOpQKPjxchMuP8 arc3.leeds.ac.uk (ED25519)
MD5:9d:1e:f0:4e:f6:ea:3e:1e:62:7d:43:61:e4:ff:c3:3d arc3.leeds.ac.uk (RSA)
MD5:c2:b1:9a:c1:44:aa:ba:a1:db:c6:b7:d4:48:9d:74:89 arc3.leeds.ac.uk (ECDSA)
MD5:27:1a:96:81:ab:02:1f:45:ca:08:21:3f:09:09:65:06 arc3.leeds.ac.uk (ED25519)
```
