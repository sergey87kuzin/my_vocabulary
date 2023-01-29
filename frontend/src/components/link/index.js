import React from "react"
import { NavLink } from 'react-router-dom'
import styles from './style.module.css'
import cn from 'classnames'

const LinkComponent = ({ exact, href, title, className, activeclassname }) => {
  return <NavLink exact={exact} activeclassname={activeclassname} className={cn(styles.link, className)} to={href}>
    {title}
  </NavLink>
}

export default LinkComponent