import './App.css';

function App() {
  return (
    <div className='login-box'>
      <h2>Login</h2>
      <form>
          <div className='user-box'>
            <input type="text"  />
            <label >username</label>
            
          </div>
          <div className='user-box'>
            <input type="password" />
            <label> password</label>
          </div>
          <div className='boton-form'>
              <button className='submit'>Subimt</button>
              <div className='submt'>
                Don't have an account?
              </div>
          </div>
      </form>

    </div>
  );
}

export default App;
