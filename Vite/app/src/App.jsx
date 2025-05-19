import { Fragment, useState } from 'react'
import './App.css'

function App() {
    const [isClicked, setIsClicked] = useState(false);
    return (
      <div>
        <>
          <h1>Vite + React</h1>
          <div className="card">
            <button onClick={() => setIsClicked(!isClicked)}>
              {isClicked ? "클릭되었습니다." : "클릭해 주세요."}
            </button>
          </div>
          <p className="read-the-docs">
            Click on the Vite and React logos to learn more
          </p>
        </>
      </div>
    )

}

export default App
