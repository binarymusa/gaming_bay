// // retrieves a reference to an HTML element with the id "navLinks" using the getElementById method.
//


// login page js.......................

var nameError = document.getElementById('name-error');
var phoneError = document.getElementById('phone-error');
var emailError = document.getElementById('email-error');
// var messageError = document.getElementById('message-error');
var submitError = document.getElementById('submit-error');
var passwdError = document.getElementById('Password-error');
var passwd2Error = document.getElementById('Password2-error');

function  validateName(){
    // is a DOM (Document Object Model) method that retrieves an element with the specified ID from the HTML document
    // .value gets the input element
    var name= document.getElementById('contact-name').value;

    // inner.html allows you to access or modify the HTML content within an element
    // cheks if the field is empty
    if( name.length == 0 ){
        nameError.innerHTML = 'Name is required!';
        return false;
    }

    // \s: This part matches a single space character
    // [A-Za-z]+: This part matches one or more alphabetic characters for the last name
    // ! negates the result
    if(!name.match(/^[A-Za-z]*\s{1}[A-Za-z]*$/)){
        nameError.innerHTML = 'write full name!';
        return false;

    }

    // displays a check icon to show correct input
    nameError.innerHTML = '<i class="fa fa-check-circle"></i>';
    return true;
}

function  validatephone(){
    var phone= document.getElementById('contact-phone').value;

    if( phone.length == 0 ){
        phoneError.innerHTML = 'phone is required!';
        return false;
    }

    // checks if value of no is up to 10digits
    if(phone.length !== 10 ){
        phoneError.innerHTML = '10 digits expected!';
        return false;
    }

    // checks pattern of phone number
    if(!phone.match(/^[0-9]{10}$/)){
        phoneError.innerHTML = 'only digits!';
        return false;
    }

    phoneError.innerHTML = '<i class="fa fa-check-circle"></i>';
    return true;

}

function  validateEmail(){
    var email= document.getElementById('contact-email').value;

    if( email.length == 0 ){
        emailError.innerHTML = 'email is required!';
        return false;
    }


    if(!email.match(/^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{3,4})$/)){
        emailError.innerHTML = 'Invalid email!';
        return false;
    }

    emailError.innerHTML = '<i class="fa fa-check-circle"></i>';
    return true;
}


function validatepassword(){
    var password= document.getElementById('contact-password').value;

    if( password.length == 0 ){
        passwdError.innerHTML = 'password  is required!';
        return false;
    }

    if( password.length < 10 ){
        passwdError.innerHTML = 'password length should be 10 characters';
        return false;
    }

    passwdError.innerHTML = '<i class="fa fa-check-circle"></i>';
    return true;
}

function validatepassword2(){
    var password2= document.getElementById('contact-password2').value;

    if( password2.length == 0 ){
        passwd2Error.innerHTML = 'password is required!';
        return false;
    }

    passwd2Error.innerHTML = '<i class="fa fa-check-circle"></i>';
    return true;
}

function passwordequality(){
    var password= document.getElementById('contact-password').value;
    var password2= document.getElementById('contact-password2').value;

    if(password != password2){
        passwd2Error.innerHTML ='password 2 does not match first password';
        return false;
    }


}
// function  validatemessage(){
//     var message= document.getElementById('contact-message').value;

//     var required = 30;
//     var left = required - message.length;

//     if(left > 0){
//         messageError.innerHTML = left + 'more characters required';
//         return false;
//     }
    
//     messageError.innerHTML = '<i class="fa fa-check-circle"></i>';
//     return true;
// }

function validateform(){
    if(!validateName() || !validatephone() || !validateEmail() || !validatepassword() || !validatepassword2()){
        submitError.style.display = 'block'
        submitError.innerHTML = '<i class="fa fa-exclamation-triangle"></i> Please fix error to submit'
        setTimeout(function(){submitError.style.display= 'none';},3000)
        return false;
    }
        
}



