###unit testing is a way to test the units in our 
### program that we want to check if it gives the desired output  or not ,
##that were expecting.to check this we have to do unit testing
##in industry the projects are big and different people do different changes 
##to keep it in track and debug we do unit testing
##each module will have its own test file that we can run test with
#it doesnt run in production before production we have to run it to check if its working or not
#autopep8



def do_stuf(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "please enter number"
    except ValueError as err:
        return err


