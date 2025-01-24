document.querySelector('#footerBtn').addEventListener('click', (event) => {
  
  event.preventDefault();

  
  const emailInput = document.querySelector('#emailInput').value.trim();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(emailInput)) {
      alert("Please enter a valid email address!");
      return;
  }

  
  const footerBtn = document.querySelector('#footerBtn');
  footerBtn.disabled = true;

  
  document.querySelector('#footerMail').innerHTML = `
    <div style="background-color:black; text-align:center; padding: 20px; border-radius: 10px; font-size: 20px">
      <h1 style="color: white;">Thank you! Your submission has been received!</h1>
    </div>
  `;

  
  document.querySelector('#dataForm').submit();
});
