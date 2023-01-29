import './App.css';
import { Routes, Route } from 'react-router-dom'
import { Nav } from "./components/index"
import { Main, New, Familiar, Known, EngRus} from "./pages"

function App() {
  return (
    <div className="App">
      <Nav />
      <Routes>
        <Route exact path='/' element={<Main />} />
        <Route exact path='/new_words' element={<New />} />
        <Route exact path='/familiar_words' element={<Familiar />} />
        <Route exact path='/known_words' element={<Known />} />
        <Route exact path='/translate_to_russian' element={
          <EngRus
            shuffle={false}
            from={"english"}
            to={"russian"}
          />} />
        <Route exact path='/translate_to_english' element={
          <EngRus
            shuffle={false}
            from={"russian"}
            to={"english"}
          />} />
        <Route exact path='/translate_to_russian' element={
          <EngRus
            shuffle={false}
            from={"english"}
            to={"russian"}
          />} />
        <Route exact path='/word_from_letters' element={
          <EngRus
            shuffle={true}
            from={"english"}
            to={"english"}
          />} />
        <Route exact path='/word_from_letters_rus' element={
          <EngRus
            shuffle={true}
            from={"russian"}
            to={"russian"}
          />} />
      </Routes>
    </div>
  );
}

export default App;
