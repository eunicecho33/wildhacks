import {Fragment} from 'react';
function ListGroup(){
    
    return (
        <Fragment>
            <h3> Select what is most Important to you 
                 <br />Click in the order of importance
            </h3>
            <ul className="list-group">
                <li className="list-group-item">School Safety</li>
                <li  className="list-group-item"> Highschool Graduation Rate</li>
                <li className="list-group-item">College enrollment rate</li>
                <li className="list-group-item">SAT Score</li>
                <li className="list-group-item">For later</li>
            </ul>
        </Fragment>
    );

}

export default ListGroup;