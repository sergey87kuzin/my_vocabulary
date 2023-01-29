import styles from "./style.module.css"
import api from "../../api"
import React from "react"
import {RadioLine} from "../../components"


const InputCard = ({id, question, ans}) => {
    const [answer, setAnswer] = React.useState()
    const [result, setResult] = React.useState('Неверно')
    const [formData, setFormData] = React.useState(
        {isKnown: "is_known"}
    )

    function handleSubmit(event) {
        // поскольку сабмит обновляет форму, это обновление надо отключать
        event.preventDefault()
        // submitToApi(formData)
        let body = {
            id: id,
            answer: answer
        }
        api.checkAnswer({body})
        .then(res => {
            console.log(res)
            setResult(res)
            if ( res === "Верно" ) {
                window.location.reload()
            }
        })
    }

    function handleChange(event) {
        setFormData(prevFormData => {
            const {name, value, type, checked} = event.target
            api.setNewWordStatus({id: id, field: value})
            return {
                ...prevFormData,
                // если мы динамически записываем атрибут, берем его в квадратные скобки
                // элементу формы удобно присвоить имя такое же, как в машине состояний у объекта
                [name]: type === "checkbox" ? checked : value
            }
        })
    }

    return (
        <div className={styles.card}>
            <div className={styles.cardText}>
                <form
                    onSubmit={handleSubmit}
                >
                    <label htmlFor="translate">
                        {question} - 
                    </label>
                    <input
                        className="input_for_ex"
                        id="translate"
                        type="text"
                        onChange={e => {
                            const value = e.target.value
                            setAnswer(value)
                        }}
                    />
                    <button>
                        проверить
                    </button>
                </form>
                <p>       {result}       </p>
            </div>
            <RadioLine
                isKnown={formData.isKnown}
                handleChange={(event) => {handleChange(event)}}
            />
        </div>
    )
}

export default InputCard