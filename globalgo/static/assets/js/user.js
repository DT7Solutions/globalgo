

function reset(){
    $("#Username").val('')
    $("#email").val('')
    $("#password").val('')
    $("#confirm_password").val('')
    $("#phone").val('')
}

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
            // show_success(response['message'])
            window.location.href = '/student_view/';
            reset()
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
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


function resetlogin() {
    $("#email").val('');
    $("#password").val('');
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
                resetlogin();
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

function verifaccount(){
    const getemail = $("#email_id").val()

    var formData = new FormData()
    formData.append('email', getemail)
    
   
    $.ajax({
        url: '/reset_password_link/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}



function changePassword(){
    const old_password = $("#old_password").val()
    const new_password = $("#new_password").val()
    const confirm_password = $("#confirm_password").val()

    var formData = new FormData()
    formData.append('oldPassword', old_password)
    formData.append('newPassword', new_password)
    formData.append('confirmPassword', confirm_password)
    
   
    $.ajax({
        url: '/change_user_password/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}

function userResertPassword(){
    const new_password = $("#new_password").val()
    const confirm_password = $("#confirm_password").val()

    var formData = new FormData()
    formData.append('newPassword', new_password)
    formData.append('confirmPassword', confirm_password)
    
    $.ajax({
        url: '/passwordReset/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            show_success(response['message'])
        },
        error: function(response){
            // show_error(response.responseJSON['message'])
        }
        
    })
}