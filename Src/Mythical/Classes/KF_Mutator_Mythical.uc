class KF_Mutator_Mythical extends KFMutator;
/**
* This function can be used to parse the command line parameters when a server
* starts up
*/
function InitMutator(string Options, out string ErrorMessage)
{
	local Actor A;
	foreach AllActors( class 'Actor', A )
	{
//		`log( A );
	}
}


event PreBeginPlay()
{
	`log("PreBeginPlay Was Called");
}


event PostBeginPlay()
{
	`log("PostBeginPlay Was Called");
}