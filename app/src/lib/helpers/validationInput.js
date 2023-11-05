
export default class validationInput {

    constructor(){
        console.log("Validation input")
    }

    static notEmpty(inputText){
        if(inputText.length <= 0){

            return false
        }

        return true
    }


}