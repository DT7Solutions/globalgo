
function creatuser(){
    const username = $("#username").val()
    const phone = $("#phonenumber").val()
    const emailId = $("#email").val()
    const password = $("#password").val()
    const confirm_password = $("#confirm_password").val()
    
    var formData = new FormData()
    formData.append('username', username)
    formData.append('phone', phone)
    formData.append('emailId', emailId)
    formData.append('password', password)
    formData.append('confirm_password', confirm_password)

    $.ajax({
        url: '/user_register/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
            reset()
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}


function reset(){
    $("#Username").val('')
    $("#email").val('')
    $("#password").val('')
    $("#confirm_password").val('')
    $("#phone").val('')
}



function creatstaff(){
    const username = $("#username").val()
    const phone = $("#phonenumber").val()
    const emailId = $("#email").val()
    const password = $("#password").val()
    const confirm_password = $("#confirm_password").val()
    
    var formData = new FormData()
    formData.append('username', username)
    formData.append('phone', phone)
    formData.append('emailId', emailId)
    formData.append('password', password)
    formData.append('confirm_password', confirm_password)

    $.ajax({
        url: '/staff_register/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
            reset()
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}


function reset(){
    $("#Username").val('')
    $("#email").val('')
    $("#password").val('')
    $("#confirm_password").val('')
    $("#phone").val('')
}


function resetlogin(){
    $("#email").val('')
    $("#password").val('')
}


function userlogin(){
    const email = $("#email").val()
    const password = $("#password").val()
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
    
    var formData = new FormData()
    formData.append('emailId', email)
    formData.append('password', password)
    formData.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
   
    $.ajax({
        url: '/sigin/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            if (response.redirect_url) {
                resetlogin()
                window.location.href = response.redirect_url;
            } else {
                
            }
            
            
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}



function verifyotp(){
    const getotp = $("#otp").val()

    var formData = new FormData()
    formData.append('enterOtp', getotp)
    
   
    $.ajax({
        url: '/otp_verification/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            if (response) {
                window.location.href = '/change_password/';
            } else {
                alert("fail to redirect")
            }
            
            
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}



// function creatuser(){
  
//     const first_name = $("#first_name").val()
//     const last_name = $("#last_name").val()
//     const username = $("#Username").val()
//     const phone = $("#phonenumber").val()
//     const emailId = $("#email").val()
//     const password = $("#password").val()
//     const confirm_password = $("#confirm_password").val()
//     const dateofBirth = $("#dob").val()
//     const address = $("#address").val()
//     const user_type = $("#user_type :selected").val()
//     const pincode = $("#pincode").val()
//     const user_id = $('#user_id').val()
//     const profileImage = $("#profile_image")[0].files[0]

//     var formData = new FormData()
//     formData.append('user_id',user_id)
//     formData.append('first_name', first_name)
//     formData.append('username', username)
//     formData.append('last_name', last_name)
//     formData.append('phone', phone)
//     formData.append('emailId', emailId)
//     formData.append('password', password)
//     formData.append('confirm_password', confirm_password)
//     formData.append('dateofBirth', dateofBirth)
//     formData.append('address', address)
//     formData.append('user_type', user_type)
//     formData.append('pincode', pincode)
//     formData.append('file', profileImage)

//     $.ajax({
//         url: '/user_register/',
//         method: 'POST',
//         data: formData,
//         processData: false,
//         contentType: false,
//         success: function(response){
//             show_success(response['message'])
//             reset()
//         },
//         error: function(response){
//             show_error(response.responseJSON['message'])
//         }
        
//     })
// }


// function reset(){
//     $("#first_name").val('')
//     $("#last_name").val('')
//     $("#phone").val('')
//     $("#emailId").val('')
//     $("#dob").val('')
//     $("#address").val('')
//     $("#user_type").val('').trigger('change')
//     $("#pincode").val('')
//     $('#user_id').val('')
//     $("#profile_image").val('')
    
// }

// function validate(){
//     var literal;
//         literal = {
//             req1: { selector: $("#first_name"), required: {message: 'Please enter the first name'} },
//             req2: { selector: $("#last_name"), required: {message: 'Please enter the last number'} },
//             req3: { selector: $("#phone"), regex: {value: /^(\+\d{1,3}[- ]?)?\d{10}$/, message: 'Please enter a valid 10-digit contact number'} },
//             req4: { selector: $("#emailId"), regex: {value: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/, message: 'Please enter a valid email address'} },
//             req5: { selector: $("#dob"), required: {message: 'Please select the DOB'} },
//             req6: { selector: $("#address"), required: {message: 'Please select the branch'} },
//             req7: { selector: $("#user_type"), required: {message: 'Please select the user type'} },
            
//         }
// }