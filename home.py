template = """
<!doctype html>
<html>
  <head>

    <link  type="text/css" rel="stylesheet" href="/static/game.css" />
    <script src="/static/game.js"></script>
    <title>XSS game</title>

  </head>
  <body>
    <h1 id="level-title">Warning: You are entering the Damn XSS Vulnerabilities</h1>

    <div id="instructions">

    <h2>Welcome, challenger!</h2>
    <a href="//www.google.com/about/appsecurity/learning/xss/index.html">Cross-site
      scripting</a> (XSS) is a type of security vulnerability commonly found in web applications. It occurs when an attacker successfully injects malicious scripts into web pages viewed by other users. These scripts can be used to steal sensitive information such as cookies or session data, manipulate the content of the web page, or redirect users to malicious websites. 

    <br><br>
    Understanding XSS is crucial for web developers and security professionals to protect applications from these attacks. By learning how XSS works and implementing effective mitigation techniques, such as input validation, output encoding, and deploying Content Security Policy (CSP), developers can build more secure web applications that safeguard user data and maintain trust.
    <br><br>

    
      <h2>Training progress:</h2>
      <table id="training-progress">
      
        <tr>
          <td class="level-name">Level 1: 
            <a href="/level1"> Hello, world of XSS</a></td>
          <td class="level-status">
            
              &#x2713; 
            
          </td>
        </tr>
      
        <tr>
          <td class="level-name">Level 2: 
            <a href="/level2"> Persistence is key</a></td>
          <td class="level-status">
            
              &#x2713; 
            
          </td>
        </tr>
      
        <tr>
          <td class="level-name">Level 3: 
            <a href="/level3"> That sinking feeling...</a></td>
          <td class="level-status">
            
              &#x2713; 
            
          </td>
        </tr>
      
        <tr>
          <td class="level-name">Level 4: 
            <a href="/level4"> Context matters</a></td>
          <td class="level-status">
            
              &#x2713; 
            
          </td>
        </tr>
      
        <tr>
          <td class="level-name">Level 5: 
            <a href="/level5"> Breaking protocol</a></td>
          <td class="level-status">
            
              &#x2713; 
            
          </td>
        </tr>
      
        <tr>
          <td class="level-name">Level 6: 
            <a href="/level6"> Follow the <span id='rabbit'>&#128007;</span></a></td>
          <td class="level-status">
            
              &#x2713; 
            
          </td>
        </tr>
      
      </table>
    
    <br>
    <h4><a href="#" onclick="this.style.display = 'none'; document.getElementById('intro-faq').style.display='block'; return false">?</a></h4>
    <div id="intro-faq" style="display: none">
      <h4>What's this all about?</h4>
      This security game consists of several levels resembling real-world applications
which are vulnerable to XSS - your task will be to find the problem and attack
the apps, similar to what an evil hacker might do.
      <br><br>
      XSS bugs are common because they have a nasty habit of popping up wherever a webapp
      deals with untrusted input. Our motivation is to highlight common coding patterns
      which lead to XSS to help you spot them in your code.

      <h4>Who can play?</h4>
      The game is designed primarily for developers working on Web
applications who do not specialize in security. If you're a connoisseur of
online hacking challenges you'll find the first few levels quite easy, but
you just might learn something useful along the way.
      <br><br>
      You'll need a modern browser which supports Javascript and cookies.

      <h4>Is it possible to cheat at this game?</h4>
      Yes, since this is a browser-based game, you will be able to cheat by
      messing with the page internals in developer tools or editing HTTP traffic.
      <br><br>
      However, we're sure that you won't have to resort to that -- there are
      hints and source to guide you. And as your teacher once told you:
      <i>you would only be cheating yourself</i> ;-)

      <h4>How will I know when I'm done?</h4>
      There <b>will</b> be cake at the end of the test.
      <br><br>

    </div>
  </body>
</html>
"""

def get_home_page():
    return template