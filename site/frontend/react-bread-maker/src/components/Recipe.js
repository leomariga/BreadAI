import React from 'react'
import { Form, TextArea } from 'semantic-ui-react'


export const Recipe = ({ recipe }) => {
  return <Form>
            <TextArea 
                placeholder='Tell us more'
                value={recipe}
                label='Recipe'
                style={{ minHeight: 400 }}
            />
        </Form>
}
