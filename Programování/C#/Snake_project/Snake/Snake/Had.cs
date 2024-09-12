using System.Windows.Media;
using System.Windows.Shapes;
using System.Windows.Controls;

namespace Snake {
    public class Had {
        public int x, y;
        public Rectangle hlava = new Rectangle();
        public Had(int x, int y) { this.x = x; this.y = y; }
        public void HadovaPozice() {
            hlava.Width = 10;
            hlava.Height = 10;
            hlava.Fill = Brushes.SpringGreen;
            Canvas.SetLeft(hlava, x);
            Canvas.SetTop(hlava, y);
        }
    }
}
