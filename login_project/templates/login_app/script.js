
    $(document).ready(function () {
      $('#registrationForm').submit(function (event) {
        event.preventDefault();
        var password = $('#password').val();
        var reEnterPassword = $('#reEnterPassword').val();
        if (password.length < 8) {
          alert('Password must be at least 8 characters long.');
          return;
        }
        if (password !== reEnterPassword) {
          alert('Passwords do not match.');
          return;
        }
        if (!validatePhone()) {
          return;
        }
        // Perform your form submission logic here, like AJAX request or form validation
        // For demo, let's just display form data
        var formData = $(this).serializeArray();
        var formObject = {};
        $.each(formData, function (index, element) {
          formObject[element.name] = element.value;
        });
        console.log(formObject);
        alert('Form submitted. Check console for data.');

        // Reset the form
        $('#registrationForm')[0].reset();
      });
    });

    function validatePhone() {
      var phone = $('#phoneNumber').val();
      var phoneError = $('#phoneError');
      phoneError.text('');
      var phoneRegex = /^[0-9]{10}$/;
      if (phone.trim() === '') {
        phoneError.text('Phone number is required');
        return false;
      } else if (!phoneRegex.test(phone)) {
        phoneError.text('Invalid phone number format');
        return false;
      }
      return true;
    }