#how to write unit test (AAA)
#check if its working the way we though it would
#check functionality of our program
#unit as an individual function .independently
#test written for testing a unit of code
#one unit test runs independently of any other unit test
#external dependecies are managed with doubles(mocks fakes stubs)
#connecting to webserver external sites
#should complete in miliseconds


#Arrange Act Asser each individual should have in program or individual unit

#test doubles used in external db, web,api, library, network
#we check our code not theirs because 
#easy to simulate various scenarios (all global scenarios)

#mocks ,fakes ,stubs
#-mocks replace external interface
#mocks are not used for checking function behaviour
#or return values from the function call? 
#check if the funciton called or not check what parameters called
#right no times, right no of parameter,right parameters, how many times,
#what parameters are passed right set of call right function right aparameters or not

#stubs
#genereate predefined outputs
#programmed stub to return a success, failure or Exception
#success,failure,as coded or exception
#checks the behaviour of code undr test in case of 
#these return values

#fakes
#connects to local server instead of going to internet
#insetead of actually going to the internet to a local implementation
#check teh begaviour with respect to the actual data it receives from te server
#check it before hand locally instead of going to real world
#create specifically for this test
#how the code behaves when it really gets load f data
#does not make dependent on other 
#ech can be independe
