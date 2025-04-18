import { Dispatch, SetStateAction } from "react";
import "../styles/Input.css";

interface InputProps {
  start: string;
  setStart: Dispatch<SetStateAction<string>>;
  end: string;
  setEnd: Dispatch<SetStateAction<string>>;
  calculate: () => void;
}


export default function Input({ start, setStart, end, setEnd, calculate }: InputProps) {
  const handleStartInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setStart(e.target.value);
  }

  const handleEndInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEnd(e.target.value);
  }
  
  return (
    <div id="input-container">
      <span>Find the shortest paths from</span>
      <div id="inputs">
        <input 
          value={start} 
          onInput={handleStartInput}
          placeholder={`from`}
        />
        <span id="arrow">→</span>
        <input 
          value={end}
          onInput={handleEndInput} 
          placeholder={`to`}
        />
      </div>
      <div id="input-button" onClick={calculate}>Go!</div>
    </div>
  );
}