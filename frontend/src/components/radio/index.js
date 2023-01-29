import React from "react"
import styles from "./style.module.css"

const Radio = ({name, label, checked, onChange}) => {
    return (
        <div>
            <input 
                type="radio"
                id={name}
                name="isKnown"
                value={name}
                checked={checked}
                onChange={onChange}
            />
            <label htmlFor={name}>{label}</label>
        </div>
    )
}

export default Radio