import React, { PureComponent } from "react";
import { Grid, Segment, Image } from "semantic-ui-react";
import "./HomeBody.scss";
import CustomUpload from "./CustomUpload";

class HomeBody extends PureComponent {
  render() {
    return (
      <div className="home-body">
        <Grid stackable columns={2}>
          <Grid.Column>
            <Segment>
              <CustomUpload />
            </Segment>
          </Grid.Column>
          <Grid.Column>
            <Segment>
              <Image src="https://react.semantic-ui.com/images/wireframe/paragraph.png" />
            </Segment>
          </Grid.Column>
        </Grid>
      </div>
    );
  }
}

export default HomeBody;
