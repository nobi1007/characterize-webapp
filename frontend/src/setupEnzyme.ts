import { configure,shallow,mount,render } from 'enzyme';
import EnzymeAdapter from 'enzyme-adapter-react-16';
import test from 'ts-jest'

configure({ adapter: new EnzymeAdapter() });

export { shallow, mount, render,test };
