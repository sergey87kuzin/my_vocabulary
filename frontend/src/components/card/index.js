import React from "react"
import RadioLine from "../radio-line"
import styles from "./style.module.css"
import api from "../../api"

const WordCard = ({ id, english = "go", russian = "идти", isKnown="unknown"}) => {
    const [formData, setFormData] = React.useState(
        {isKnown: isKnown}
    )

    console.log(formData)

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
                <h3>{english}</h3>
                <h3> - </h3>
                <h3>{russian}</h3>
            </div>
            <RadioLine
                isKnown={formData.isKnown}
                handleChange={(event) => {handleChange(event)}}
            />
        </div>
    )
}

export default WordCard