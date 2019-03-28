/*
state is a javascript object which is going to contain some sort of data 
state is dynamic and it keeps changing with time 
we output dynamic data in cury brackets in jsx e.g { name }
this === refers to the component in which the function is in
whenever we change the state that component renders the template to the dom

we dont change the state directly in react e.g we dont do this this.state.name ='Edgar'
instead we use a function to change state. this function is called this.setState(). inside the function we pass in an 
object to change the state like this.setState({})

the onChange event is used to detect whatever the user is typing in the input field and then change the state based 
on what the user is typing. the onChange event fires everytime there is a change of value inside the input field 

when we submit a form the default action is for the page to reload / refreshes. we prevent that default behaviour 
by running e.preventDefault();

*/

class App extends Component {
    
    state = {
		name: 'Frank',
		age: 25
    }
    
    handleClick = (e) => {
        this.setState({name:'Mwesigwa', age:30})
    }

    handleMouseOver = (e) => {
        console.log(e)
    }

    handleChange = (e) => {
        this.setState({name:e.target.value})
    }

    handleSubmit = (e) => {
        e.preventDefault();
        console.log('Form Submitted', this.state.name)
    }
	
	render(){
		return(
			<div className="container">
				<h1>Hello Ninja</h1>
				<h2>my name is : {this.state.name}</h2>
				<h3>my age is : {this.state.age}</h3>
                <button onClick={this.handleClick}>Click Me</button>
                <button onMouseOver={}>Hover Me</button>

                <div>
                    <h2>My Name is : {this.state.name} </h2>
                    <form onSubmit={this.handleSubmit}>
                        <input type="text" onChange={this.handleChange} />
                        <button>Submit</button>
                    </form>
                </div>

			</div>
		
		)
	}
}

export default App