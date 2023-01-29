import React from "react"
import { Radio } from "../index"
import styles from "./style.module.css"

const RadioLine = ({ isKnown, handleChange }) => {
    console.log(isKnown)
    return (
        <div>
            <form>
                <fieldset className={styles.isKnownForm}>
                    <legend>слово известно?</legend>
                    <Radio 
                        name="is_new"
                        label="неизвестно"
                        checked={isKnown === "is_new"}
                        onChange={(event) => handleChange(event)}
                    />
                    <Radio 
                        name="is_well_known"
                        label="частично известно"
                        checked={isKnown === "is_well_known"}
                        onChange={(event) => handleChange(event)}
                    />
                    <Radio 
                        name="is_known"
                        label="хорошо известно"
                        checked={isKnown === "is_known"}
                        onChange={(event) => handleChange(event)}
                    />
                </fieldset>
            </form>
        </div>
    )
}

export default RadioLine