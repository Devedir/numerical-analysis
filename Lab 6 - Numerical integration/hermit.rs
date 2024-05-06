use std::f32::consts;

const H: f32 = 0.001;

fn f(x: f32) -> f32 {
    consts::E.powf(-(x*x)) * f32::cos(x)
}

fn main() {
    println!("{:?}", f(0.0));
    println!("{:?}", f(1.0));
    println!("{:?}", f(2.0));
    println!("{:?}", f(4.0));
}
