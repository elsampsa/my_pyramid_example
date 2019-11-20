### Local docker run

Create a python package in your main dir with
```
./make.bash
```

Then get some files into this directory by running 
```
./get.bash
```

Then follow the comments in the Dockerfile for creating an image & running it

### Deploy to Heroku
Install heroku cli (once):
```
sudo snap install --classic heroku
```

Create the app in Heroku web gui.  Let's call it "kokkelis".  Then do:
```
heroku container:login
```

After that, this works:
```
heroku container:push -a kokkelis web
container:release -a kokkelis web
```

Now you should be able to open your app in https://dashboard.heroku.com/apps

### Misc
Remember to run 
```
docker image prune
```
every now and then..
