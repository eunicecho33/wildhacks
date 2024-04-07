import {Fragment} from 'react';
function ListGroup(){
    
    return (
        <Fragment>
            <h3> Select what is most Important to you 
                 <br />Fill in the order of importance
            </h3>
            <ul className="list-group">
                <li className="list-group-item">
                    School Safety 
                    <input type="number" />
                </li>
                <li className="list-group-item">
                    Highschool Graduation Rate 
                    <input type="number" />
                </li>
                <li className="list-group-item">
                    College enrollment rate 
                    <input type="number" />
                </li>
                <li className="list-group-item">
                    SAT Score 
                    <input type="number" />
                </li>
                <li className="list-group-item">
                    For later 
                    <input type="number" />
                </li>
            </ul>
        </Fragment>
    );

}

export default ListGroup;