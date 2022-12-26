//juego piedra pepel o tijera?
function playRound(){ 
    choice()
        //If player win
if ((playerSelection === "paper" && computerSelection === "rock") || (playerSelection === "rock" &&   computerSelection === "scissors") || (playerSelection === "scissors" && computerSelection === "paper")){
        return `The player won! ${playerSelection} beats ${computerSelection}`;  
     
    }  //If computer win
    else if ((playerSelection === "rock" && computerSelection === "paper") || (playerSelection === "scissors" && computerSelection === "rock") || (playerSelection === "paper" && computerSelection === "scissors")){
        return `The computer won!  ${computerSelection} beats ${playerSelection}`;  
    }   // If its a tie
    else {
        return "It´s a tie!";
    }
}

function choice (){
    
    playerSelection = prompt("Que opcion elegis? Rock, Paper or Scissors?");
    playerSelection = playerSelection.toLowerCase();
    computerSelection = computerPlay();
    console.log(`The computer chose: ${computerSelection}`);
    console.log(`You chose: ${playerSelection}`);
    
} 

function computerPlay() {
    const options = ["scissors" , "rock" , "paper"];
        return options[Math.floor(Math.random()* options.length)];
}


let playerSelection;
let computerSelection;

for (let i = 0 ; i < 5; i++){
    console.log(playRound());
}

function playRound(player, computer){ 
    choice()
    // Aca player y computer tienen los valores con que se llamó la función
    // y no los valores que mutó choice() que son playerSelection y computerSelection

    //If player win
    if ((player === "paper" && computer === "rock") || (player === "rock" && computer === "scissors") || (player === "scissors" && computer === "paper")){
        return `The player won! ${player} beats ${computer}`;  
    }
      //If computer win
    else if ((player === "rock" && computer === "paper") || (player === "scissors" && computer === "rock") || (player === "paper" && computer === "scissors")){
        return `The computer won!  ${computer} beats ${player}`;  
    }
    // If its a tie
    else {
        return "It´s a tie!";
    }
}

function choice (){
    
    playerSelection = prompt("Que opción elegís? Rock, Paper or Scissors?");
    playerSelection = playerSelection.toLowerCase();
    computerSelection = computerPlay();
    console.log(`The computer chose: ${computerSelection}`);
    console.log(`You chose: ${playerSelection}`);
    
} 

function computerPlay() {
    const options = ["scissors" , "rock" , "paper"];
        return options[Math.floor(Math.random()* options.length)];
}


let playerSelection;
let computerSelection;

for (let i = 0 ; i < 5; i++){
    console.log(playRound(playerSelection, computerSelection));
}

