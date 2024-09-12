using System.Windows.Shapes;
using System.Windows.Media;
using System.Windows.Controls;

namespace Snake
{
    public class Jidlo {
        public int x, y;
        public Ellipse mys = new Ellipse();
        public Jidlo(int x, int y) { this.x = x; this.y = y;}
        public void MysiPozice() {
            mys.Width = 10;
            mys.Height = 10;
            mys.Fill = Brushes.WhiteSmoke;
            Canvas.SetLeft(mys, x);
            Canvas.SetTop(mys, y);
        }
    }
}
